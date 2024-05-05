from tqdm import tqdm
import time

def loading():
    # Total number of iterations
    total_iterations = 100

    # Initialize the progress bar
    progress_bar = tqdm(total=total_iterations, desc="Loading", position=0,colour="#00ff00")

    # Simulate some task
    for i in range(total_iterations):
        # Do some work here
        time.sleep(0.1)
        # Update the progress bar
        progress_bar.update(1)

    # Close the progress bar
    progress_bar.close()

    print('\033[1;92m' " Loading complete!")
