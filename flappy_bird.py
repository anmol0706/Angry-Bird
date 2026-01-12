import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame

class FlappyBird:
    def __init__(self, root):
        self.root = root
        self.root.title("🐦 Flappy Bird")
        self.root.resizable(False, False)
        
        # Game variables - Smoother physics
        self.bird_y = 250
        self.bird_velocity = 0
        self.gravity = 0.4  # Reduced for smoother falling
        self.jump_power = -8  # Adjusted for smoother jumps
        self.pipe_speed = 2  # Slower pipes for better gameplay
        
        self.pipes = []
        self.score = 0
        self.high_score = 0  # Track high score
        self.game_over = False
        self.game_started = False
        self.clouds = []  # For decorative clouds
        
        # Initialize pygame mixer for music
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("angry-birds-drill-128-ytshorts.savetube.me.mp3")
            pygame.mixer.music.set_volume(0.5)  # Set volume to 50%
            pygame.mixer.music.play(-1)  # Loop forever (-1)
            self.music_enabled = True
        except Exception as e:
            print(f"Could not load music: {e}")
            self.music_enabled = False
        
        # Create canvas with gradient sky
        self.canvas = tk.Canvas(root, width=400, height=600, bg="#87CEEB")
        self.canvas.pack()
        
        # Add decorative clouds
        self.create_clouds()
        
        # Load and resize bird image
        try:
            bird_image = Image.open("image.png")
            bird_image = bird_image.resize((40, 40), Image.Resampling.LANCZOS)
            self.bird_photo = ImageTk.PhotoImage(bird_image)
            self.bird = self.canvas.create_image(65, self.bird_y + 15, image=self.bird_photo)
        except Exception as e:
            # Fallback to circle if image fails to load
            print(f"Could not load bird image: {e}")
            self.bird_photo = None
            self.bird = self.canvas.create_oval(50, self.bird_y, 80, self.bird_y + 30, 
                                               fill="#FFD700", outline="#FFA500", width=2)
        
        # Score display with shadow effect
        self.score_shadow = self.canvas.create_text(202, 52, 
                                                     text="Score: 0", 
                                                     font=("Arial", 24, "bold"),
                                                     fill="black")
        self.score_text = self.canvas.create_text(200, 50, 
                                                  text="Score: 0", 
                                                  font=("Arial", 24, "bold"),
                                                  fill="white")
        
        # High score display
        self.high_score_text = self.canvas.create_text(200, 80,
                                                       text="Best: 0",
                                                       font=("Arial", 14, "bold"),
                                                       fill="#FFD700")
        
        # Instructions
        self.start_text = self.canvas.create_text(200, 300,
                                                  text="Press SPACE to start!\n\nSPACE = Jump\nR = Restart\nM = Mute/Unmute",
                                                  font=("Arial", 18, "bold"),
                                                  fill="white")
        
        # Bind space key to jump and R key to restart
        self.root.bind("<space>", self.jump)
        self.root.bind("<r>", self.restart_game)
        self.root.bind("<R>", self.restart_game)
        self.root.bind("<m>", self.toggle_music)
        self.root.bind("<M>", self.toggle_music)
        
        # Create ground
        self.ground = self.canvas.create_rectangle(0, 550, 400, 600, 
                                                   fill="#8B4513", outline="")
    
    def create_clouds(self):
        """Create decorative clouds in the background"""
        cloud_positions = [(80, 150), (250, 120), (350, 180), (150, 400), (320, 450)]
        for x, y in cloud_positions:
            # Create fluffy cloud with multiple circles
            cloud = []
            cloud.append(self.canvas.create_oval(x, y, x+40, y+25, fill="white", outline=""))
            cloud.append(self.canvas.create_oval(x+15, y-10, x+45, y+15, fill="white", outline=""))
            cloud.append(self.canvas.create_oval(x+30, y, x+60, y+25, fill="white", outline=""))
            self.clouds.extend(cloud)
    
    def jump(self, event=None):
        """Make the bird jump"""
        if not self.game_started:
            # Start the game
            self.game_started = True
            self.canvas.delete(self.start_text)
            self.game_loop()
        
        if not self.game_over:
            # Make bird jump
            self.bird_velocity = self.jump_power
    
    def toggle_music(self, event=None):
        """Toggle background music on/off"""
        if self.music_enabled:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
    
    def create_pipe(self):
        """Create a new pipe obstacle with improved visuals"""
        gap = 180  # Larger gap for easier, smoother gameplay
        height = random.randint(100, 350)
        
        # Top pipe with darker outline for 3D effect
        top_pipe = self.canvas.create_rectangle(400, 0, 450, height,
                                                fill="#2E8B57", outline="#1a5c37", width=3)
        
        # Bottom pipe with darker outline
        bottom_pipe = self.canvas.create_rectangle(400, height + gap, 450, 550,
                                                   fill="#2E8B57", outline="#1a5c37", width=3)
        
        # Store both pipes together
        self.pipes.append({
            'top': top_pipe,
            'bottom': bottom_pipe,
            'x': 400,
            'scored': False
        })
    
    def move_pipes(self):
        """Move all pipes to the left"""
        for pipe in self.pipes:
            # Move pipe left with configurable speed
            pipe['x'] -= self.pipe_speed
            self.canvas.coords(pipe['top'], pipe['x'], 0, pipe['x'] + 50, 
                             self.canvas.coords(pipe['top'])[3])
            self.canvas.coords(pipe['bottom'], pipe['x'], 
                             self.canvas.coords(pipe['bottom'])[1],
                             pipe['x'] + 50, 550)
            
            # Check if bird passed the pipe
            if not pipe['scored'] and pipe['x'] < 50:
                pipe['scored'] = True
                self.score += 1
                
                # Update high score
                if self.score > self.high_score:
                    self.high_score = self.score
                
                # Update score displays with animation effect
                self.canvas.itemconfig(self.score_shadow, text=f"Score: {self.score}")
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                self.canvas.itemconfig(self.high_score_text, text=f"Best: {self.high_score}")
                
                # Brief score flash animation
                self.canvas.itemconfig(self.score_text, fill="#FFD700")
                self.root.after(100, lambda: self.canvas.itemconfig(self.score_text, fill="white"))
        
        # Remove pipes that are off screen
        self.pipes = [p for p in self.pipes if p['x'] > -50]
    
    def check_collision(self):
        """Check if bird hit pipe or ground"""
        if self.bird_photo:
            # Image-based bird (center position)
            bird_x = 65
            bird_y = self.bird_y + 15
            bird_left = bird_x - 20
            bird_right = bird_x + 20
            bird_top = bird_y - 20
            bird_bottom = bird_y + 20
        else:
            # Circle-based bird
            bird_coords = self.canvas.coords(self.bird)
            bird_left = bird_coords[0]
            bird_top = bird_coords[1]
            bird_right = bird_coords[2]
            bird_bottom = bird_coords[3]
        
        # Check if hit ground or ceiling
        if bird_bottom >= 550 or bird_top <= 0:
            return True
        
        # Check collision with pipes
        for pipe in self.pipes:
            pipe_top = self.canvas.coords(pipe['top'])
            pipe_bottom = self.canvas.coords(pipe['bottom'])
            
            # If bird is in the x-range of pipe
            if bird_right > pipe['x'] and bird_left < pipe['x'] + 50:
                # Check if bird hit top or bottom pipe
                if bird_top < pipe_top[3] or bird_bottom > pipe_bottom[1]:
                    return True
        
        return False
    
    def game_loop(self):
        """Main game loop"""
        if self.game_over:
            return
        
        # Apply gravity
        self.bird_velocity += self.gravity
        self.bird_y += self.bird_velocity
        
        # Move bird (handle both image and circle)
        if self.bird_photo:
            # For image (uses center position)
            self.canvas.coords(self.bird, 65, self.bird_y + 15)
        else:
            # For circle (uses corner positions)
            self.canvas.coords(self.bird, 50, self.bird_y, 80, self.bird_y + 30)
        
        # Create new pipes
        if len(self.pipes) == 0 or self.pipes[-1]['x'] < 200:
            self.create_pipe()
        
        # Move pipes
        self.move_pipes()
        
        # Check for collision
        if self.check_collision():
            self.end_game()
            return
        
        # Continue game loop at 60 FPS (16ms) for smooth gameplay
        self.root.after(16, self.game_loop)
    
    def end_game(self):
        """End the game with enhanced visuals"""
        self.game_over = True
        
        # Semi-transparent overlay
        self.canvas.create_rectangle(0, 0, 400, 600,
                                     fill="black",
                                     stipple="gray50",
                                     tag="gameover")
        
        # Game over panel
        self.canvas.create_rectangle(50, 150, 350, 450,
                                     fill="#2c3e50",
                                     outline="#ecf0f1",
                                     width=3,
                                     tag="gameover")
        
        # Display game over message
        self.canvas.create_text(200, 200,
                               text="GAME OVER!",
                               font=("Arial", 36, "bold"),
                               fill="#e74c3c",
                               tag="gameover")
        
        # Display scores
        self.canvas.create_text(200, 260,
                               text=f"Score: {self.score}",
                               font=("Arial", 24, "bold"),
                               fill="white",
                               tag="gameover")
        
        self.canvas.create_text(200, 300,
                               text=f"Best Score: {self.high_score}",
                               font=("Arial", 20, "bold"),
                               fill="#FFD700",
                               tag="gameover")
        
        # Medal based on score
        if self.score >= 20:
            medal = "🏆 GOLD MEDAL!"
            color = "#FFD700"
        elif self.score >= 10:
            medal = "🥈 SILVER MEDAL!"
            color = "#C0C0C0"
        elif self.score >= 5:
            medal = "🥉 BRONZE MEDAL!"
            color = "#CD7F32"
        else:
            medal = "Keep Trying!"
            color = "#95a5a6"
        
        self.canvas.create_text(200, 345,
                               text=medal,
                               font=("Arial", 18, "bold"),
                               fill=color,
                               tag="gameover")
        
        # Restart instructions
        self.canvas.create_text(200, 400,
                               text="Press R to Restart!",
                               font=("Arial", 18, "bold"),
                               fill="#3498db",
                               tag="gameover")
    
    def restart_game(self, event=None):
        """Restart the game"""
        # Reset game variables (keep high_score!)
        self.bird_y = 250
        self.bird_velocity = 0
        self.score = 0
        self.game_over = False
        self.game_started = False
        
        # Clear all pipes
        for pipe in self.pipes:
            self.canvas.delete(pipe['top'])
            self.canvas.delete(pipe['bottom'])
        self.pipes = []
        
        # Delete game over messages
        self.canvas.delete("gameover")
        
        # Reset bird position (handle both image and circle)
        if self.bird_photo:
            self.canvas.coords(self.bird, 65, self.bird_y + 15)
        else:
            self.canvas.coords(self.bird, 50, self.bird_y, 80, self.bird_y + 30)
        
        # Reset score displays
        self.canvas.itemconfig(self.score_shadow, text="Score: 0")
        self.canvas.itemconfig(self.score_text, text="Score: 0")
        self.canvas.itemconfig(self.high_score_text, text=f"Best: {self.high_score}")
        
        # Show start instructions again
        self.start_text = self.canvas.create_text(200, 300,
                                                  text="Press SPACE to start!\n\nSPACE = Jump\nR = Restart\nM = Mute/Unmute",
                                                  font=("Arial", 18, "bold"),
                                                  fill="white")

# Create and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = FlappyBird(root)
    root.mainloop()
