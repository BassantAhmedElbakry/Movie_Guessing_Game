# Movie guessing game

# Import libraries
import pygame
import random

# Screen dimensions: Width  = 1000, Height = 750
size = (1000, 750)

# Background color
background_color = (50, 150, 230)

# Initialization of the game screen
pygame.init()
# Set the Height and the width of the game screen
screen = pygame.display.set_mode(size)
# Start position of the game screen
start_position = pygame.Vector2(screen.get_width() // 2, 20)

# Load a font for Heading
Heading_font = pygame.font.Font(None, 36)

# Print: "Arabic movies in English"
Hello_text1 = Heading_font.render("Arabic movies in English", True, "white")
Hello_text1_rect = Hello_text1.get_rect()
Hello_text1_rect.center = (start_position)

# Print: "Gussing the Movie"
Hello_text2 = Heading_font.render("Gussing the Movie", True, "white")
Hello_text2_rect = Hello_text2.get_rect()
Hello_text2_rect.center = (start_position[0], 50)

############### the Movies ###############
Movies = ["Taimur and Shafiqa", "The suit", "Made in Egypt", 
          "At Misr station", "Hassan and Morcos", "Yacoubian Building",
          "X Large", "Italy war","Karmoz war",
          "Diamond dust", "I Love you", "Captain Hema",
          "Omar and Salma", "The Guest", "Before the Summer Crowds",
          "Mafia", "Girls love", "The Island",
          "Andaleeb Al Doqqi", "Matab Senay", "Sorry for the Disturbance",
          "Bikya", "Aboud Ala El Hedoud", "Thieves in Thailand",
          "Meraty w Zawgaty", "Teita Rahiba", "Khalty Faransa",
          "Ya Ana Ya Khalty", "Hamam fi Amsterdam", "El Dezel",
          "Africano", "El Markeb", "The Passage",
          "Saeedi in the American University", "Sons of Rizk", "365 Days of happiness",
          "Helm Aziz", "The Blue Elephant", "Noor Eieny",
          "Okal", "El Khaliyya", "El khalbous",
          "Ellembi 8 Gega", "Elli Bali Balak", "Call Mama",
          "Ellembi", "Ereys Men Jhh Amenyh", "Morgan Ahmed Morgan",
          "Eyaal Habeebah", "Amn Dawlat", "Zaza",
          "Mohami Kholaa", "Ayez Haqqi", "The Prince of Darkness",
          "Thieves in KG2", "El saher", "Awdet Al-Nadla",
          "Gana El Bian El Taly", "Tomn Dastet Ashrar", "Al Thalatha Yashtaghaloonaha",
          "Hareem Kareem", "Miss Mammy", "Aldada Dodi",
          "Zaky Chan", "Zarf Tarek", "She Made Me a Criminal"]

# Select random movie from Movies List
selectedMovie = random.randrange(0, len(Movies))

# Create a list to store guessed letters
guessed_letters = ['_ ' if char != ' ' else '  ' for char in Movies[selectedMovie]]

# Wrong guessings
wrong_guesses = 0
max_wrong_guesses = 5

# Print: "Congratulations! You guessed the movie!"
Congrats_text = Heading_font.render("Congratulations! You guessed the movie!", True, "Green")
Congrats_text_rect = Congrats_text.get_rect()
Congrats_text_rect.center = (start_position[0], (size[1] - (size[1] // 3)))

# Print Game over message
Gameover_text = Heading_font.render(f"Game over! The correct movie was: {Movies[selectedMovie]}", True, "Red")
Gameover_text_rect = Gameover_text.get_rect()
Gameover_text_rect.center = (start_position[0], (size[1] - (size[1] // 3)))

# Print Wrong Guess message
wrongGuess_text = Heading_font.render(f"Wrong guess! You have only {max_wrong_guesses} guesses!!", True, "Yellow")
wrongGuess_text_rect = wrongGuess_text.get_rect()
wrongGuess_text_rect.center = (start_position[0], (size[1] // 2))

##### The Game Loop #####
while True:
    # Fill the screen with the background color 
    screen.fill(background_color)
    
    # Display Hello texts to the game screen
    screen.blit(Hello_text1, Hello_text1_rect)
    screen.blit(Hello_text2, Hello_text2_rect)
    
    # Display the current state of the movie (with dashes and guessed letters)
    Movie = ''.join(guessed_letters)
    Movie_text = Heading_font.render(Movie, True, "white")
    screen.blit(Movie_text, (start_position[0] - len(Movie) * 4.5, 200))
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            # Get the user's input
            user_input = pygame.key.name(event.key).lower()
            if len(user_input) == 1 and (user_input.isalpha() or user_input.isnumeric()):
                if user_input.lower() in Movies[selectedMovie].lower():
                    for index, char in enumerate(Movies[selectedMovie].lower()):
                        if char == user_input.lower():
                            guessed_letters[index] = user_input
                else:
                    wrong_guesses += 1
                    # Display Wrong Guess message
                    screen.blit(Heading_font.render(f"Wrong guess! {max_wrong_guesses - wrong_guesses} guesses left.", True, "Yellow"),
                    wrongGuess_text_rect)
                    # Update the display to show the wrong guess message
                    pygame.display.flip()
                    pygame.time.delay(1500)

                # Check if the player has guessed all the letters
                if "_ " not in guessed_letters:
                    # Clear the area where the movie display text is rendered before drawing
                    pygame.draw.rect(screen, background_color, (start_position[0] - len(Movie) * 7, 200, 800, 60))
                    # Rebuild movie display to ensure it includes the last guessed character
                    Movie = ''.join(guessed_letters)
                    
                    # Redraw the movie title and display the Congrats message
                    screen.blit(Hello_text1, Hello_text1_rect)
                    screen.blit(Hello_text2, Hello_text2_rect)
                    Movie_text = Heading_font.render(Movie, True, "white")
                    screen.blit(Movie_text, (start_position[0] - len(Movie) * 7, 200))
                    
                    # Display Congrats message
                    screen.blit(Congrats_text, Congrats_text_rect)
                    # Update the display
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    pygame.quit()
                    quit()
                
                # Check if the player has run out of guesses
                if wrong_guesses >= max_wrong_guesses:
                    # Display Game over text
                    screen.blit(Gameover_text, Gameover_text_rect)
                    # Update the display
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    pygame.quit()
                    quit()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
quit()
            
    
    

