﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on November 24, 2023, at 15:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_wordlist
import random

# list of psuedowords - LEVER
word_list = ['psythos','addaign', 'gyepset', 'oppasms','ridaps','sclueeze', 
'addlaim'] 
random.shuffle(word_list)

# list of repititions - LEVER
rep_times = [1,2,3,4,5,5,7]                     
random.shuffle(rep_times)

# WW is a list of first psuedowords each repeated n times, and so on.
WW = []
W_train = []
for i in range(len(word_list)):
    WW.extend([word_list[i]] * rep_times[i])
    W_train.extend([word_list[i]] * rep_times[i]) 

combined = list(zip(WW, W_train))
random.shuffle(combined)
WW, W_train = zip(*combined)
WW = list(WW)
W_train = list(W_train)   # psuedoword list for tarining phase
len_W_train = len(W_train)  

#----------------------------

# Familiarity pseudowords
psuedo_lists = []
list_size = 3         # how many pseudowords in a trial - LEVER

# number of trials = total num words/ num words in one trial
num_new_lists = len(WW)/list_size 

# make 'unique' (no repeat) list of words from WW into 'psuedo_lists'
while len(WW) >= list_size:
  
      first_elem = random.choice(WW)
      WW.remove(first_elem)

      second_elem = random.choice(WW)
      while second_elem == first_elem:
          second_elem = random.choice(WW)
      WW.remove(second_elem)

      third_elem = random.choice(WW)
      while third_elem == first_elem or third_elem ==second_elem:
          third_elem = random.choice(WW)
      WW.remove(third_elem)
      
      psuedo_lists.append([first_elem, second_elem,third_elem])   

#-------------------------
len_trials = len(psuedo_lists)        # familiarity trials total
len_assoc_trials = len(word_list)    # association

print(psuedo_lists)
# Run 'Before Experiment' code from code

feature1 = ["Red", "Blue", "Green", "Yellow", "Orange", "Pink", 
"Black"];
shuffle(feature1)

feature2 = [1,2,3,4,5,6,7]
shuffle(feature2)

feature3 = ['e','f','g','h','i','j','k']
shuffle(feature3)

feature4 = ['!', '@', '#', '$', '%', '^', '&']
shuffle(feature4)

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'confidence'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\jadit\\OneDrive\\Desktop\\Confidence_study\\confidence_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1366, 768], fullscr=False, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instructions" ---
    text_Welcome = visual.TextStim(win=win, name='text_Welcome',
        text='Welcome',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_Instructions = visual.TextStim(win=win, name='text_Instructions',
        text='Instructions\n\nPress SPACE to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_complete = keyboard.Keyboard()
    
    # --- Initialize components for Routine "psuedowords" ---
    # Run 'Begin Experiment' code from code_wordlist
    iter = -1
    
    text_psuedoword1 = visual.TextStim(win=win, name='text_psuedoword1',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_psuedoword2 = visual.TextStim(win=win, name='text_psuedoword2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_psuedoword3 = visual.TextStim(win=win, name='text_psuedoword3',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_delay = visual.TextStim(win=win, name='text_delay',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "memory" ---
    text_instruct_memory = visual.TextStim(win=win, name='text_instruct_memory',
        text='Write down the words you just saw',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textbox_word1 = visual.TextBox2(
         win, text=None, placeholder='Type the first word here...', font='Arial',
         pos=(-0.5, 0),     letterHeight=0.04,
         size=(0.3, 0.3), borderWidth=0.5,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.5, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_word1',
         depth=-1, autoLog=True,
    )
    textbox_word2 = visual.TextBox2(
         win, text=None, placeholder='Type second word here...', font='Arial',
         pos=(0, 0),     letterHeight=0.04,
         size=(0.3, 0.3), borderWidth=0.5,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.5, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_word2',
         depth=-2, autoLog=True,
    )
    textbox_word3 = visual.TextBox2(
         win, text=None, placeholder='Type second word here...', font='Arial',
         pos=(0.5, 0),     letterHeight=0.04,
         size=(0.3, 0.3), borderWidth=0.5,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.5, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_word3',
         depth=-3, autoLog=True,
    )
    button = visual.ButtonStim(win, 
        text='Done', font='Arvo',
        pos=(0.5, -0.4),
        letterHeight=0.05,
        size=(0.2, 0.2), borderWidth=0.0,
        fillColor='darkgray', borderColor=[0.0000, 0.0000, 0.0000],
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button',
        depth=-4
    )
    button.buttonClock = core.Clock()
    text_button = visual.TextStim(win=win, name='text_button',
        text='Done',
        font='Open Sans',
        pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "train" ---
    # Run 'Begin Experiment' code from code
    iter_train = -1
    text_psuedowords = visual.TextStim(win=win, name='text_psuedowords',
        text='',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_f1 = visual.TextStim(win=win, name='text_f1',
        text='',
        font='Open Sans',
        pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_f2 = visual.TextStim(win=win, name='text_f2',
        text='',
        font='Open Sans',
        pos=(-0.2, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_f3 = visual.TextStim(win=win, name='text_f3',
        text='',
        font='Open Sans',
        pos=(0.2, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_f4 = visual.TextStim(win=win, name='text_f4',
        text='',
        font='Open Sans',
        pos=(0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "test_Instruct" ---
    text_Inst = visual.TextStim(win=win, name='text_Inst',
        text='Write down the features associated with these words',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "test" ---
    # Run 'Begin Experiment' code from code_test
    iter_test = -1
    text_test = visual.TextStim(win=win, name='text_test',
        text='',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    textbox_f1 = visual.TextBox2(
         win, text=None, placeholder='feature 1', font='Arial',
         pos=(-0.55, 0),     letterHeight=0.04,
         size=(0.3, 0.3), borderWidth=0.5,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.5, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_f1',
         depth=-2, autoLog=True,
    )
    textbox_f2 = visual.TextBox2(
         win, text=None, placeholder='feature 2', font='Arial',
         pos=(-0.2, 0),     letterHeight=0.04,
         size=(0.3, 0.3), borderWidth=0.5,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.5, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_f2',
         depth=-3, autoLog=True,
    )
    textbox_f3 = visual.TextBox2(
         win, text=None, placeholder='feature 3', font='Arial',
         pos=(0.2, 0),     letterHeight=0.04,
         size=(0.3, 0.3), borderWidth=0.5,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.5, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_f3',
         depth=-4, autoLog=True,
    )
    textbox_f4 = visual.TextBox2(
         win, text=None, placeholder='feature 4', font='Arial',
         pos=(0.55, 0),     letterHeight=0.04,
         size=(0.3, 0.3), borderWidth=0.5,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.5, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_f4',
         depth=-5, autoLog=True,
    )
    button_2 = visual.ButtonStim(win, 
        text='Done', font='Arvo',
        pos=(0.5, -0.4),
        letterHeight=0.05,
        size=(0.2, 0.2), borderWidth=0.0,
        fillColor='darkgray', borderColor=[0.0000, 0.0000, 0.0000],
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_2',
        depth=-6
    )
    button_2.buttonClock = core.Clock()
    text_button_2 = visual.TextStim(win=win, name='text_button_2',
        text='Done',
        font='Open Sans',
        pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
    # --- Initialize components for Routine "delay" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "end" ---
    text_end = visual.TextStim(win=win, name='text_end',
        text='Finished\n\nPress SPACE to end.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_end = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions.started', globalClock.getTime())
    key_resp_complete.keys = []
    key_resp_complete.rt = []
    _key_resp_complete_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [text_Welcome, text_Instructions, key_resp_complete]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Welcome* updates
        
        # if text_Welcome is starting this frame...
        if text_Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Welcome.frameNStart = frameN  # exact frame index
            text_Welcome.tStart = t  # local t and not account for scr refresh
            text_Welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Welcome.started')
            # update status
            text_Welcome.status = STARTED
            text_Welcome.setAutoDraw(True)
        
        # if text_Welcome is active this frame...
        if text_Welcome.status == STARTED:
            # update params
            pass
        
        # if text_Welcome is stopping this frame...
        if text_Welcome.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_Welcome.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_Welcome.tStop = t  # not accounting for scr refresh
                text_Welcome.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_Welcome.stopped')
                # update status
                text_Welcome.status = FINISHED
                text_Welcome.setAutoDraw(False)
        
        # *text_Instructions* updates
        
        # if text_Instructions is starting this frame...
        if text_Instructions.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_Instructions.frameNStart = frameN  # exact frame index
            text_Instructions.tStart = t  # local t and not account for scr refresh
            text_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Instructions.started')
            # update status
            text_Instructions.status = STARTED
            text_Instructions.setAutoDraw(True)
        
        # if text_Instructions is active this frame...
        if text_Instructions.status == STARTED:
            # update params
            pass
        
        # *key_resp_complete* updates
        waitOnFlip = False
        
        # if key_resp_complete is starting this frame...
        if key_resp_complete.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_complete.frameNStart = frameN  # exact frame index
            key_resp_complete.tStart = t  # local t and not account for scr refresh
            key_resp_complete.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_complete, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_complete.started')
            # update status
            key_resp_complete.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_complete.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_complete.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_complete.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_complete.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_complete_allKeys.extend(theseKeys)
            if len(_key_resp_complete_allKeys):
                key_resp_complete.keys = _key_resp_complete_allKeys[-1].name  # just the last key pressed
                key_resp_complete.rt = _key_resp_complete_allKeys[-1].rt
                key_resp_complete.duration = _key_resp_complete_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions.stopped', globalClock.getTime())
    # check responses
    if key_resp_complete.keys in ['', [], None]:  # No response was made
        key_resp_complete.keys = None
    thisExp.addData('key_resp_complete.keys',key_resp_complete.keys)
    if key_resp_complete.keys != None:  # we had a response
        thisExp.addData('key_resp_complete.rt', key_resp_complete.rt)
        thisExp.addData('key_resp_complete.duration', key_resp_complete.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=len_trials, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "psuedowords" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('psuedowords.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_wordlist
        
        # store the trial word list into separate words
        iter = iter + 1
        psuedoword1, psuedoword2, psuedoword3 = psuedo_lists[iter]
        
        
        
        # store data
        thisExp.addData('psuedoword1', psuedoword1)
        thisExp.addData('psuedoword2', psuedoword2)
        thisExp.addData('psuedoword3', psuedoword3)
        
        
        
        
        
        
        text_psuedoword1.setText(psuedoword1)
        text_psuedoword2.setText(psuedoword2)
        text_psuedoword3.setText(psuedoword3)
        # keep track of which components have finished
        psuedowordsComponents = [text_psuedoword1, text_psuedoword2, text_psuedoword3, text_delay]
        for thisComponent in psuedowordsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "psuedowords" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_psuedoword1* updates
            
            # if text_psuedoword1 is starting this frame...
            if text_psuedoword1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_psuedoword1.frameNStart = frameN  # exact frame index
                text_psuedoword1.tStart = t  # local t and not account for scr refresh
                text_psuedoword1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_psuedoword1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_psuedoword1.started')
                # update status
                text_psuedoword1.status = STARTED
                text_psuedoword1.setAutoDraw(True)
            
            # if text_psuedoword1 is active this frame...
            if text_psuedoword1.status == STARTED:
                # update params
                pass
            
            # if text_psuedoword1 is stopping this frame...
            if text_psuedoword1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_psuedoword1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_psuedoword1.tStop = t  # not accounting for scr refresh
                    text_psuedoword1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_psuedoword1.stopped')
                    # update status
                    text_psuedoword1.status = FINISHED
                    text_psuedoword1.setAutoDraw(False)
            
            # *text_psuedoword2* updates
            
            # if text_psuedoword2 is starting this frame...
            if text_psuedoword2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_psuedoword2.frameNStart = frameN  # exact frame index
                text_psuedoword2.tStart = t  # local t and not account for scr refresh
                text_psuedoword2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_psuedoword2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_psuedoword2.started')
                # update status
                text_psuedoword2.status = STARTED
                text_psuedoword2.setAutoDraw(True)
            
            # if text_psuedoword2 is active this frame...
            if text_psuedoword2.status == STARTED:
                # update params
                pass
            
            # if text_psuedoword2 is stopping this frame...
            if text_psuedoword2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_psuedoword2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_psuedoword2.tStop = t  # not accounting for scr refresh
                    text_psuedoword2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_psuedoword2.stopped')
                    # update status
                    text_psuedoword2.status = FINISHED
                    text_psuedoword2.setAutoDraw(False)
            
            # *text_psuedoword3* updates
            
            # if text_psuedoword3 is starting this frame...
            if text_psuedoword3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                text_psuedoword3.frameNStart = frameN  # exact frame index
                text_psuedoword3.tStart = t  # local t and not account for scr refresh
                text_psuedoword3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_psuedoword3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_psuedoword3.started')
                # update status
                text_psuedoword3.status = STARTED
                text_psuedoword3.setAutoDraw(True)
            
            # if text_psuedoword3 is active this frame...
            if text_psuedoword3.status == STARTED:
                # update params
                pass
            
            # if text_psuedoword3 is stopping this frame...
            if text_psuedoword3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_psuedoword3.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_psuedoword3.tStop = t  # not accounting for scr refresh
                    text_psuedoword3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_psuedoword3.stopped')
                    # update status
                    text_psuedoword3.status = FINISHED
                    text_psuedoword3.setAutoDraw(False)
            
            # *text_delay* updates
            
            # if text_delay is starting this frame...
            if text_delay.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                text_delay.frameNStart = frameN  # exact frame index
                text_delay.tStart = t  # local t and not account for scr refresh
                text_delay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_delay, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_delay.started')
                # update status
                text_delay.status = STARTED
                text_delay.setAutoDraw(True)
            
            # if text_delay is active this frame...
            if text_delay.status == STARTED:
                # update params
                pass
            
            # if text_delay is stopping this frame...
            if text_delay.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_delay.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_delay.tStop = t  # not accounting for scr refresh
                    text_delay.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_delay.stopped')
                    # update status
                    text_delay.status = FINISHED
                    text_delay.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in psuedowordsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "psuedowords" ---
        for thisComponent in psuedowordsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('psuedowords.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "memory" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('memory.started', globalClock.getTime())
        textbox_word1.reset()
        textbox_word1.setText('')
        textbox_word2.reset()
        textbox_word2.setText('')
        textbox_word3.reset()
        textbox_word3.setText('')
        # reset button to account for continued clicks & clear times on/off
        button.reset()
        # keep track of which components have finished
        memoryComponents = [text_instruct_memory, textbox_word1, textbox_word2, textbox_word3, button, text_button]
        for thisComponent in memoryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "memory" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_instruct_memory* updates
            
            # if text_instruct_memory is starting this frame...
            if text_instruct_memory.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_instruct_memory.frameNStart = frameN  # exact frame index
                text_instruct_memory.tStart = t  # local t and not account for scr refresh
                text_instruct_memory.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_instruct_memory, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_instruct_memory.started')
                # update status
                text_instruct_memory.status = STARTED
                text_instruct_memory.setAutoDraw(True)
            
            # if text_instruct_memory is active this frame...
            if text_instruct_memory.status == STARTED:
                # update params
                pass
            
            # *textbox_word1* updates
            
            # if textbox_word1 is starting this frame...
            if textbox_word1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_word1.frameNStart = frameN  # exact frame index
                textbox_word1.tStart = t  # local t and not account for scr refresh
                textbox_word1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_word1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_word1.started')
                # update status
                textbox_word1.status = STARTED
                textbox_word1.setAutoDraw(True)
            
            # if textbox_word1 is active this frame...
            if textbox_word1.status == STARTED:
                # update params
                pass
            
            # *textbox_word2* updates
            
            # if textbox_word2 is starting this frame...
            if textbox_word2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_word2.frameNStart = frameN  # exact frame index
                textbox_word2.tStart = t  # local t and not account for scr refresh
                textbox_word2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_word2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_word2.started')
                # update status
                textbox_word2.status = STARTED
                textbox_word2.setAutoDraw(True)
            
            # if textbox_word2 is active this frame...
            if textbox_word2.status == STARTED:
                # update params
                pass
            
            # *textbox_word3* updates
            
            # if textbox_word3 is starting this frame...
            if textbox_word3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_word3.frameNStart = frameN  # exact frame index
                textbox_word3.tStart = t  # local t and not account for scr refresh
                textbox_word3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_word3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_word3.started')
                # update status
                textbox_word3.status = STARTED
                textbox_word3.setAutoDraw(True)
            
            # if textbox_word3 is active this frame...
            if textbox_word3.status == STARTED:
                # update params
                pass
            # *button* updates
            
            # if button is starting this frame...
            if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button.frameNStart = frameN  # exact frame index
                button.tStart = t  # local t and not account for scr refresh
                button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button.started')
                # update status
                button.status = STARTED
                button.setAutoDraw(True)
            
            # if button is active this frame...
            if button.status == STARTED:
                # update params
                pass
                # check whether button has been pressed
                if button.isClicked:
                    if not button.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button.timesOn.append(button.buttonClock.getTime())
                        button.timesOff.append(button.buttonClock.getTime())
                    elif len(button.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button.timesOff[-1] = button.buttonClock.getTime()
                    if not button.wasClicked:
                        # end routine when button is clicked
                        continueRoutine = False
                    if not button.wasClicked:
                        # run callback code when button is clicked
                        pass
            # take note of whether button was clicked, so that next frame we know if clicks are new
            button.wasClicked = button.isClicked and button.status == STARTED
            
            # *text_button* updates
            
            # if text_button is starting this frame...
            if text_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_button.frameNStart = frameN  # exact frame index
                text_button.tStart = t  # local t and not account for scr refresh
                text_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_button.started')
                # update status
                text_button.status = STARTED
                text_button.setAutoDraw(True)
            
            # if text_button is active this frame...
            if text_button.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in memoryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "memory" ---
        for thisComponent in memoryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('memory.stopped', globalClock.getTime())
        trials.addData('textbox_word1.text',textbox_word1.text)
        trials.addData('textbox_word2.text',textbox_word2.text)
        trials.addData('textbox_word3.text',textbox_word3.text)
        trials.addData('button.numClicks', button.numClicks)
        if button.numClicks:
           trials.addData('button.timesOn', button.timesOn)
           trials.addData('button.timesOff', button.timesOff)
        else:
           trials.addData('button.timesOn', "")
           trials.addData('button.timesOff', "")
        # the Routine "memory" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed len_trials repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_train = data.TrialHandler(nReps=len_assoc_trials, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_train')
    thisExp.addLoop(loop_train)  # add the loop to the experiment
    thisLoop_train = loop_train.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_train.rgb)
    if thisLoop_train != None:
        for paramName in thisLoop_train:
            globals()[paramName] = thisLoop_train[paramName]
    
    for thisLoop_train in loop_train:
        currentLoop = loop_train
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_train.rgb)
        if thisLoop_train != None:
            for paramName in thisLoop_train:
                globals()[paramName] = thisLoop_train[paramName]
        
        # --- Prepare to start Routine "train" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('train.started', globalClock.getTime())
        # Run 'Begin Routine' code from code
        iter_train = iter_train +1
        
        # store data
        thisExp.addData('psuedoword_train', word_list[iter_train])
        thisExp.addData('feature1', feature1[iter_train])
        thisExp.addData('feature2', feature2[iter_train])
        thisExp.addData('feature3', feature3[iter_train])
        thisExp.addData('feature4', feature4[iter_train])
        
        
        text_psuedowords.setText(word_list[iter_train])
        text_f1.setColor(feature1[iter_train], colorSpace='rgb')
        text_f1.setText(feature1[iter_train])
        text_f2.setText(feature2[iter_train])
        text_f3.setText(feature3[iter_train])
        text_f4.setText(feature4[iter_train])
        # keep track of which components have finished
        trainComponents = [text_psuedowords, text_f1, text_f2, text_f3, text_f4]
        for thisComponent in trainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "train" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_psuedowords* updates
            
            # if text_psuedowords is starting this frame...
            if text_psuedowords.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_psuedowords.frameNStart = frameN  # exact frame index
                text_psuedowords.tStart = t  # local t and not account for scr refresh
                text_psuedowords.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_psuedowords, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_psuedowords.started')
                # update status
                text_psuedowords.status = STARTED
                text_psuedowords.setAutoDraw(True)
            
            # if text_psuedowords is active this frame...
            if text_psuedowords.status == STARTED:
                # update params
                pass
            
            # if text_psuedowords is stopping this frame...
            if text_psuedowords.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_psuedowords.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_psuedowords.tStop = t  # not accounting for scr refresh
                    text_psuedowords.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_psuedowords.stopped')
                    # update status
                    text_psuedowords.status = FINISHED
                    text_psuedowords.setAutoDraw(False)
            
            # *text_f1* updates
            
            # if text_f1 is starting this frame...
            if text_f1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_f1.frameNStart = frameN  # exact frame index
                text_f1.tStart = t  # local t and not account for scr refresh
                text_f1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_f1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_f1.started')
                # update status
                text_f1.status = STARTED
                text_f1.setAutoDraw(True)
            
            # if text_f1 is active this frame...
            if text_f1.status == STARTED:
                # update params
                pass
            
            # if text_f1 is stopping this frame...
            if text_f1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_f1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_f1.tStop = t  # not accounting for scr refresh
                    text_f1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_f1.stopped')
                    # update status
                    text_f1.status = FINISHED
                    text_f1.setAutoDraw(False)
            
            # *text_f2* updates
            
            # if text_f2 is starting this frame...
            if text_f2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_f2.frameNStart = frameN  # exact frame index
                text_f2.tStart = t  # local t and not account for scr refresh
                text_f2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_f2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_f2.started')
                # update status
                text_f2.status = STARTED
                text_f2.setAutoDraw(True)
            
            # if text_f2 is active this frame...
            if text_f2.status == STARTED:
                # update params
                pass
            
            # if text_f2 is stopping this frame...
            if text_f2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_f2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_f2.tStop = t  # not accounting for scr refresh
                    text_f2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_f2.stopped')
                    # update status
                    text_f2.status = FINISHED
                    text_f2.setAutoDraw(False)
            
            # *text_f3* updates
            
            # if text_f3 is starting this frame...
            if text_f3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_f3.frameNStart = frameN  # exact frame index
                text_f3.tStart = t  # local t and not account for scr refresh
                text_f3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_f3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_f3.started')
                # update status
                text_f3.status = STARTED
                text_f3.setAutoDraw(True)
            
            # if text_f3 is active this frame...
            if text_f3.status == STARTED:
                # update params
                pass
            
            # if text_f3 is stopping this frame...
            if text_f3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_f3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_f3.tStop = t  # not accounting for scr refresh
                    text_f3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_f3.stopped')
                    # update status
                    text_f3.status = FINISHED
                    text_f3.setAutoDraw(False)
            
            # *text_f4* updates
            
            # if text_f4 is starting this frame...
            if text_f4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_f4.frameNStart = frameN  # exact frame index
                text_f4.tStart = t  # local t and not account for scr refresh
                text_f4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_f4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_f4.started')
                # update status
                text_f4.status = STARTED
                text_f4.setAutoDraw(True)
            
            # if text_f4 is active this frame...
            if text_f4.status == STARTED:
                # update params
                pass
            
            # if text_f4 is stopping this frame...
            if text_f4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_f4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_f4.tStop = t  # not accounting for scr refresh
                    text_f4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_f4.stopped')
                    # update status
                    text_f4.status = FINISHED
                    text_f4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "train" ---
        for thisComponent in trainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('train.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed len_assoc_trials repeats of 'loop_train'
    
    
    # --- Prepare to start Routine "test_Instruct" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('test_Instruct.started', globalClock.getTime())
    # keep track of which components have finished
    test_InstructComponents = [text_Inst]
    for thisComponent in test_InstructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "test_Instruct" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Inst* updates
        
        # if text_Inst is starting this frame...
        if text_Inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Inst.frameNStart = frameN  # exact frame index
            text_Inst.tStart = t  # local t and not account for scr refresh
            text_Inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Inst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Inst.started')
            # update status
            text_Inst.status = STARTED
            text_Inst.setAutoDraw(True)
        
        # if text_Inst is active this frame...
        if text_Inst.status == STARTED:
            # update params
            pass
        
        # if text_Inst is stopping this frame...
        if text_Inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_Inst.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_Inst.tStop = t  # not accounting for scr refresh
                text_Inst.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_Inst.stopped')
                # update status
                text_Inst.status = FINISHED
                text_Inst.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_InstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "test_Instruct" ---
    for thisComponent in test_InstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('test_Instruct.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    loop_test = data.TrialHandler(nReps=len_assoc_trials, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_test')
    thisExp.addLoop(loop_test)  # add the loop to the experiment
    thisLoop_test = loop_test.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_test.rgb)
    if thisLoop_test != None:
        for paramName in thisLoop_test:
            globals()[paramName] = thisLoop_test[paramName]
    
    for thisLoop_test in loop_test:
        currentLoop = loop_test
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_test.rgb)
        if thisLoop_test != None:
            for paramName in thisLoop_test:
                globals()[paramName] = thisLoop_test[paramName]
        
        # --- Prepare to start Routine "test" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('test.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_test
        iter_test = iter_test +1 
        
        # store data
        thisExp.addData('psuedoword_test', word_list[iter_test])
        
        text_test.setText(word_list[iter_test])
        textbox_f1.reset()
        textbox_f1.setText('')
        textbox_f2.reset()
        textbox_f2.setText('')
        textbox_f3.reset()
        textbox_f3.setText('')
        textbox_f4.reset()
        textbox_f4.setText('')
        # reset button_2 to account for continued clicks & clear times on/off
        button_2.reset()
        # keep track of which components have finished
        testComponents = [text_test, textbox_f1, textbox_f2, textbox_f3, textbox_f4, button_2, text_button_2]
        for thisComponent in testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_test* updates
            
            # if text_test is starting this frame...
            if text_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_test.frameNStart = frameN  # exact frame index
                text_test.tStart = t  # local t and not account for scr refresh
                text_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_test, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_test.started')
                # update status
                text_test.status = STARTED
                text_test.setAutoDraw(True)
            
            # if text_test is active this frame...
            if text_test.status == STARTED:
                # update params
                pass
            
            # *textbox_f1* updates
            
            # if textbox_f1 is starting this frame...
            if textbox_f1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textbox_f1.frameNStart = frameN  # exact frame index
                textbox_f1.tStart = t  # local t and not account for scr refresh
                textbox_f1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_f1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_f1.started')
                # update status
                textbox_f1.status = STARTED
                textbox_f1.setAutoDraw(True)
            
            # if textbox_f1 is active this frame...
            if textbox_f1.status == STARTED:
                # update params
                pass
            
            # *textbox_f2* updates
            
            # if textbox_f2 is starting this frame...
            if textbox_f2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textbox_f2.frameNStart = frameN  # exact frame index
                textbox_f2.tStart = t  # local t and not account for scr refresh
                textbox_f2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_f2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_f2.started')
                # update status
                textbox_f2.status = STARTED
                textbox_f2.setAutoDraw(True)
            
            # if textbox_f2 is active this frame...
            if textbox_f2.status == STARTED:
                # update params
                pass
            
            # *textbox_f3* updates
            
            # if textbox_f3 is starting this frame...
            if textbox_f3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textbox_f3.frameNStart = frameN  # exact frame index
                textbox_f3.tStart = t  # local t and not account for scr refresh
                textbox_f3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_f3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_f3.started')
                # update status
                textbox_f3.status = STARTED
                textbox_f3.setAutoDraw(True)
            
            # if textbox_f3 is active this frame...
            if textbox_f3.status == STARTED:
                # update params
                pass
            
            # *textbox_f4* updates
            
            # if textbox_f4 is starting this frame...
            if textbox_f4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textbox_f4.frameNStart = frameN  # exact frame index
                textbox_f4.tStart = t  # local t and not account for scr refresh
                textbox_f4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_f4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_f4.started')
                # update status
                textbox_f4.status = STARTED
                textbox_f4.setAutoDraw(True)
            
            # if textbox_f4 is active this frame...
            if textbox_f4.status == STARTED:
                # update params
                pass
            # *button_2* updates
            
            # if button_2 is starting this frame...
            if button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_2.frameNStart = frameN  # exact frame index
                button_2.tStart = t  # local t and not account for scr refresh
                button_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_2.started')
                # update status
                button_2.status = STARTED
                button_2.setAutoDraw(True)
            
            # if button_2 is active this frame...
            if button_2.status == STARTED:
                # update params
                pass
                # check whether button_2 has been pressed
                if button_2.isClicked:
                    if not button_2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_2.timesOn.append(button_2.buttonClock.getTime())
                        button_2.timesOff.append(button_2.buttonClock.getTime())
                    elif len(button_2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_2.timesOff[-1] = button_2.buttonClock.getTime()
                    if not button_2.wasClicked:
                        # end routine when button_2 is clicked
                        continueRoutine = False
                    if not button_2.wasClicked:
                        # run callback code when button_2 is clicked
                        pass
            # take note of whether button_2 was clicked, so that next frame we know if clicks are new
            button_2.wasClicked = button_2.isClicked and button_2.status == STARTED
            
            # *text_button_2* updates
            
            # if text_button_2 is starting this frame...
            if text_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_button_2.frameNStart = frameN  # exact frame index
                text_button_2.tStart = t  # local t and not account for scr refresh
                text_button_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_button_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_button_2.started')
                # update status
                text_button_2.status = STARTED
                text_button_2.setAutoDraw(True)
            
            # if text_button_2 is active this frame...
            if text_button_2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test" ---
        for thisComponent in testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('test.stopped', globalClock.getTime())
        loop_test.addData('textbox_f1.text',textbox_f1.text)
        loop_test.addData('textbox_f2.text',textbox_f2.text)
        loop_test.addData('textbox_f3.text',textbox_f3.text)
        loop_test.addData('textbox_f4.text',textbox_f4.text)
        loop_test.addData('button_2.numClicks', button_2.numClicks)
        if button_2.numClicks:
           loop_test.addData('button_2.timesOn', button_2.timesOn)
           loop_test.addData('button_2.timesOff', button_2.timesOff)
        else:
           loop_test.addData('button_2.timesOn', "")
           loop_test.addData('button_2.timesOff', "")
        # the Routine "test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "delay" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('delay.started', globalClock.getTime())
        # keep track of which components have finished
        delayComponents = [text]
        for thisComponent in delayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "delay" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "delay" ---
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('delay.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed len_assoc_trials repeats of 'loop_test'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    key_resp_end.keys = []
    key_resp_end.rt = []
    _key_resp_end_allKeys = []
    # keep track of which components have finished
    endComponents = [text_end, key_resp_end]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_end* updates
        
        # if text_end is starting this frame...
        if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_end.frameNStart = frameN  # exact frame index
            text_end.tStart = t  # local t and not account for scr refresh
            text_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_end.started')
            # update status
            text_end.status = STARTED
            text_end.setAutoDraw(True)
        
        # if text_end is active this frame...
        if text_end.status == STARTED:
            # update params
            pass
        
        # if text_end is stopping this frame...
        if text_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_end.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_end.tStop = t  # not accounting for scr refresh
                text_end.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_end.stopped')
                # update status
                text_end.status = FINISHED
                text_end.setAutoDraw(False)
        
        # *key_resp_end* updates
        waitOnFlip = False
        
        # if key_resp_end is starting this frame...
        if key_resp_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_end.frameNStart = frameN  # exact frame index
            key_resp_end.tStart = t  # local t and not account for scr refresh
            key_resp_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_end.started')
            # update status
            key_resp_end.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_end.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_end.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_end.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_end_allKeys.extend(theseKeys)
            if len(_key_resp_end_allKeys):
                key_resp_end.keys = _key_resp_end_allKeys[-1].name  # just the last key pressed
                key_resp_end.rt = _key_resp_end_allKeys[-1].rt
                key_resp_end.duration = _key_resp_end_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # check responses
    if key_resp_end.keys in ['', [], None]:  # No response was made
        key_resp_end.keys = None
    thisExp.addData('key_resp_end.keys',key_resp_end.keys)
    if key_resp_end.keys != None:  # we had a response
        thisExp.addData('key_resp_end.rt', key_resp_end.rt)
        thisExp.addData('key_resp_end.duration', key_resp_end.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
