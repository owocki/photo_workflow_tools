# What

Photo Workflow Tools

A suite of tools developed to make photography workflows a little more automated.  

Target Audience: Photographys who are comfortable with the command line.

# Why?

To automate (or gracefully degrade into just being more efficient) my photography post-processing process.

## Post-processing step 1: Select the best photos

One of the first elements of my photography workflow is to select which photos are *worth* post-process.  To do so, I need to select which of my set of photos to *promote* to a 'best' subset.  This is what it looked like before:

<img src='https://raw.githubusercontent.com/owocki/photo_workflow_tools/master/examples/before.gif' />

This is what it looks like after:

<img src='https://raw.githubusercontent.com/owocki/photo_workflow_tools/master/examples/after.gif' />

Much cleaner, huh?  I've gone from several keystrokes and a mouse click-and-drag to a simple button press.  Better yet, keyboard shortcuts from `y` and `n`.

## Post-processing step 2: Crop

TODO

## Post-processing step 3: Edit, markup

TODO

## Post-processing step 4: Share 

TODO

# Setup

To run this on your local environment,

1. Clone the repo
2. `cd` to the repo
3. `pip install -r requirements.txt`
4. Create a symlink from wherever you store your photos to the `static/pix` dir.  Like this: `ln -s ~/Pictures static/pix`
5. Edit `local_settings.py.example` with your own configuration, and save it as `local_settings.py` in the same dir.
6. Run the app! `./manage.py runserver 0.0.0.0:8081`
7. Open in a browser and enjoy! When you 'promote' a photo, whatever you put into `settings.PIX_WHEN_PROMOTING_APPEND_THIS_TEXT` will be appended to the filename.  From there, you can manipulate these photos on the command line using regular expressions.  Ex: `mv *.promoted.JPG ../bestof/`

<!-- Google Analytics -->
<img src='https://ga-beacon.appspot.com/UA-1014419-15/owocki/s3_disk_util' style='width:1px; height:1px;' >
