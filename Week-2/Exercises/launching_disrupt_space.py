# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Circle")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a 50px-radius circle
squareB = stimuli.Rectangle(size=(50, 50), colour=(0, 0, 255), position=(-50, 0) ) 
squareR = stimuli.Rectangle(size=(50, 50), colour=(255 , 0, 0), position=(50, 0) )
# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross
squareB.present(clear=True  , update=False)
squareR.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()