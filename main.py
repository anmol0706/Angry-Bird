from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Ellipse, Color, Line
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
import random

class FlappyBirdGame(Widget):
    def __init__(self, **kwargs):
        super(FlappyBirdGame, self).__init__(**kwargs)
        
        # Game variables - Improved physics
        self.bird_y = Window.height / 2
        self.bird_velocity = 0
        self.gravity = 0.5
        self.jump_power = -10
        self.pipe_speed = 3
        
        self.pipes = []
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.game_started = False
        
        # Visual elements
        self.bird_size = 40
        self.pipe_width = 60
        self.pipe_gap = 200
        
        # Load background music (optional)
        try:
            self.bg_music = SoundLoader.load('angry-birds-drill-128-ytshorts.savetube.me.mp3')
            if self.bg_music:
                self.bg_music.loop = True
                self.bg_music.volume = 0.3
        except:
            self.bg_music = None
        
        # Initialize game
        self.setup_game()
        
        # Bind touch/click events
        Window.bind(on_touch_down=self.on_touch_down)
        
    def setup_game(self):
        """Setup game elements"""
        with self.canvas:
            # Sky gradient background
            Color(0.53, 0.81, 0.92, 1)  # Sky blue
            self.background = Rectangle(pos=(0, 0), size=Window.size)
            
            # Ground
            Color(0.55, 0.27, 0.07, 1)  # Brown
            self.ground = Rectangle(pos=(0, 0), size=(Window.width, 80))
            
            # Bird
            Color(1, 0.84, 0, 1)  # Gold
            self.bird = Ellipse(pos=(100, self.bird_y), size=(self.bird_size, self.bird_size))
            
            # Bird eye (for better look)
            Color(0, 0, 0, 1)
            self.bird_eye = Ellipse(pos=(120, self.bird_y + 20), size=(8, 8))
        
        # Score label
        self.score_label = Label(
            text=f'Score: {self.score}',
            font_size='30sp',
            bold=True,
            color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'top': 0.98}
        )
        self.add_widget(self.score_label)
        
        # High score label
        self.high_score_label = Label(
            text=f'Best: {self.high_score}',
            font_size='20sp',
            bold=True,
            color=(1, 0.84, 0, 1),
            pos_hint={'center_x': 0.5, 'top': 0.93}
        )
        self.add_widget(self.high_score_label)
        
        # Instructions
        self.instruction_label = Label(
            text='Tap to Start!\n\nTap = Jump',
            font_size='24sp',
            bold=True,
            color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.instruction_label)
    
    def on_touch_down(self, window, touch):
        """Handle touch/click events"""
        if not self.game_started:
            self.start_game()
        elif not self.game_over:
            self.jump()
        elif self.game_over:
            # Check if restart button was tapped
            return
    
    def start_game(self):
        """Start the game"""
        self.game_started = True
        self.remove_widget(self.instruction_label)
        
        # Start background music
        if self.bg_music:
            self.bg_music.play()
        
        # Schedule game loop
        Clock.schedule_interval(self.update, 1/60)  # 60 FPS
        Clock.schedule_interval(self.create_pipe, 2)  # New pipe every 2 seconds
    
    def jump(self):
        """Make bird jump"""
        if not self.game_over:
            self.bird_velocity = self.jump_power
    
    def create_pipe(self, dt):
        """Create new pipe obstacle"""
        if self.game_over:
            return
        
        # Random height for gap
        gap_y = random.randint(150, int(Window.height - 250))
        
        with self.canvas:
            # Top pipe
            Color(0.18, 0.55, 0.34, 1)  # Green
            top_pipe = Rectangle(
                pos=(Window.width, gap_y + self.pipe_gap),
                size=(self.pipe_width, Window.height - gap_y - self.pipe_gap - 80)
            )
            
            # Bottom pipe
            bottom_pipe = Rectangle(
                pos=(Window.width, 80),
                size=(self.pipe_width, gap_y)
            )
            
            # Pipe outline for 3D effect
            Color(0.1, 0.36, 0.22, 1)
            top_outline = Line(rectangle=(Window.width, gap_y + self.pipe_gap,
                                         self.pipe_width, Window.height - gap_y - self.pipe_gap - 80), width=2)
            bottom_outline = Line(rectangle=(Window.width, 80, self.pipe_width, gap_y), width=2)
        
        self.pipes.append({
            'top': top_pipe,
            'bottom': bottom_pipe,
            'top_outline': top_outline,
            'bottom_outline': bottom_outline,
            'x': Window.width,
            'scored': False
        })
    
    def move_pipes(self):
        """Move pipes and check for scoring"""
        for pipe in self.pipes[:]:
            # Move pipe
            pipe['x'] -= self.pipe_speed
            
            # Update positions
            pipe['top'].pos = (pipe['x'], pipe['top'].pos[1])
            pipe['bottom'].pos = (pipe['x'], pipe['bottom'].pos[1])
            pipe['top_outline'].rectangle = (pipe['x'], pipe['top'].pos[1],
                                            self.pipe_width, pipe['top'].size[1])
            pipe['bottom_outline'].rectangle = (pipe['x'], pipe['bottom'].pos[1],
                                               self.pipe_width, pipe['bottom'].size[1])
            
            # Check if bird passed the pipe
            if not pipe['scored'] and pipe['x'] + self.pipe_width < 100:
                pipe['scored'] = True
                self.score += 1
                self.score_label.text = f'Score: {self.score}'
                
                # Update high score
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.high_score_label.text = f'Best: {self.high_score}'
            
            # Remove off-screen pipes
            if pipe['x'] < -self.pipe_width:
                self.canvas.remove(pipe['top'])
                self.canvas.remove(pipe['bottom'])
                self.canvas.remove(pipe['top_outline'])
                self.canvas.remove(pipe['bottom_outline'])
                self.pipes.remove(pipe)
    
    def check_collision(self):
        """Check for collisions"""
        bird_x = 100
        bird_y = self.bird_y
        
        # Check ground collision
        if bird_y <= 80 or bird_y >= Window.height - self.bird_size:
            return True
        
        # Check pipe collision
        for pipe in self.pipes:
            # If bird is in x-range of pipe
            if (bird_x + self.bird_size > pipe['x'] and 
                bird_x < pipe['x'] + self.pipe_width):
                
                # Get pipe heights
                bottom_pipe_top = pipe['bottom'].size[1] + 80
                top_pipe_bottom = pipe['top'].pos[1]
                
                # Check if bird hit pipe
                if bird_y < bottom_pipe_top or bird_y + self.bird_size > top_pipe_bottom:
                    return True
        
        return False
    
    def update(self, dt):
        """Main game loop"""
        if self.game_over:
            return
        
        # Apply gravity
        self.bird_velocity += self.gravity
        self.bird_y -= self.bird_velocity
        
        # Update bird position
        self.bird.pos = (100, self.bird_y)
        self.bird_eye.pos = (120, self.bird_y + 20)
        
        # Move pipes
        self.move_pipes()
        
        # Check collision
        if self.check_collision():
            self.end_game()
    
    def end_game(self):
        """End the game"""
        self.game_over = True
        Clock.unschedule(self.update)
        Clock.unschedule(self.create_pipe)
        
        # Stop music
        if self.bg_music:
            self.bg_music.stop()
        
        # Game over overlay
        with self.canvas:
            Color(0, 0, 0, 0.7)
            Rectangle(pos=(0, 0), size=Window.size)
        
        # Game over label
        game_over_label = Label(
            text='GAME OVER!',
            font_size='48sp',
            bold=True,
            color=(0.91, 0.30, 0.24, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        self.add_widget(game_over_label)
        
        # Final score
        final_score_label = Label(
            text=f'Score: {self.score}\nBest: {self.high_score}',
            font_size='30sp',
            bold=True,
            color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(final_score_label)
        
        # Medal text
        if self.score >= 20:
            medal = '🏆 GOLD!'
            medal_color = (1, 0.84, 0, 1)
        elif self.score >= 10:
            medal = '🥈 SILVER!'
            medal_color = (0.75, 0.75, 0.75, 1)
        elif self.score >= 5:
            medal = '🥉 BRONZE!'
            medal_color = (0.80, 0.50, 0.20, 1)
        else:
            medal = 'Keep Trying!'
            medal_color = (0.58, 0.65, 0.65, 1)
        
        medal_label = Label(
            text=medal,
            font_size='24sp',
            bold=True,
            color=medal_color,
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        self.add_widget(medal_label)
        
        # Restart button
        restart_btn = Button(
            text='Restart',
            font_size='24sp',
            bold=True,
            size_hint=(0.4, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            background_color=(0.20, 0.60, 0.86, 1),
            color=(1, 1, 1, 1)
        )
        restart_btn.bind(on_press=self.restart_game)
        self.add_widget(restart_btn)
    
    def restart_game(self, instance=None):
        """Restart the game"""
        # Clear everything
        self.clear_widgets()
        self.canvas.clear()
        
        # Reset variables
        self.bird_y = Window.height / 2
        self.bird_velocity = 0
        self.score = 0
        self.game_over = False
        self.game_started = False
        self.pipes = []
        
        # Reinitialize
        self.setup_game()


class FlappyBirdApp(App):
    def build(self):
        # Set window size for desktop testing
        Window.size = (400, 700)
        
        game = FlappyBirdGame()
        return game


if __name__ == '__main__':
    FlappyBirdApp().run()
