#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.2.0),
    on 九月 27, 2025, at 13:38
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.2.0'
expName = 'OnlineDemo_english_instruction'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant_number': '',
    'gender': '',
    'age': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
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
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant_number'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\29817\\Documents\\申请\\OnlineDemo_english_instruction.py',
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
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
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
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
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
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
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
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
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
    
    # --- Initialize components for Routine "start" ---
    text1 = visual.TextStim(win=win, name='text1',
        text='In this experiment, based on the given sentence sequence, \nplease type the word that is expected to appear next. \nExample:\n提示された語列1：「今日は」\n→ タイプ例：「天気が」\n\n提示された語列2：「今日は天気が」\n→ タイプ例：「いいです」\n\nThere are no correct or incorrect answers for the input words.\nPlease input the word that comes to mind based on your first impression.\nThe length of the content is not limited.\nAfter typing the single word, please press the Enter/Return key.\nThis experiment consists of a total of 60 sentences.\nIn a quiet environment, please conduct the experiment\nindependently without seeking help from others.\nWhen you are ready, press the SPACE to start the experiment.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp1 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "Loop" ---
    # Run 'Begin Experiment' code from code
    firstKeyClock = core.Clock()
    hasFirstKey = False
    shown_stim = visual.TextStim(win=win, name='shown_stim',
        text=None,
        font='Arial',
        pos=(-0.8, 0.37), draggable=False, height=0.044, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    response_instr = visual.TextStim(win=win, name='response_instr',
        text='Type the next words:',
        font='Arial',
        pos=(-0.3, -0.185), draggable=False, height=0.044, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    end_instr = visual.TextStim(win=win, name='end_instr',
        text="That\\'s the end of sentence\nNext sentence would appear after 2s",
        font='Arial',
        pos=(0, -0.185), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    tmp = visual.TextStim(win=win, name='tmp',
        text=None,
        font='Arial',
        pos=(-0.8, 0), draggable=False, height=0.044, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    underline = visual.Line(
        win=win, name='underline',
        size=(0.4, 0),
        ori=0.0, pos=(0.2, -0.222), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    underline_hint = visual.Line(
        win=win, name='underline_hint',
        size=(0.3, 0.0),
        ori=0.0, pos=(0, 0.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    textbox = visual.TextBox2(
         win, text=None, placeholder=None, font='SimSun',
         ori=0.0, pos=(0.2, -0.185), draggable=False,      letterHeight=0.044,
         size=(0.5, 0.0556), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox',
         depth=-7, autoLog=True,
    )
    
    # --- Initialize components for Routine "end" ---
    endword = visual.TextStim(win=win, name='endword',
        text="That\\'s the end of experiment.\nThis program would close automatically after 2s.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "start" ---
    # create an object to store info about Routine start
    start = data.Routine(
        name='start',
        components=[text1, key_resp1],
    )
    start.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp1
    key_resp1.keys = []
    key_resp1.rt = []
    _key_resp1_allKeys = []
    # store start times for start
    start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start.tStart = globalClock.getTime(format='float')
    start.status = STARTED
    thisExp.addData('start.started', start.tStart)
    start.maxDuration = None
    # keep track of which components have finished
    startComponents = start.components
    for thisComponent in start.components:
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
    
    # --- Run Routine "start" ---
    thisExp.currentRoutine = start
    start.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text1* updates
        
        # if text1 is starting this frame...
        if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text1.frameNStart = frameN  # exact frame index
            text1.tStart = t  # local t and not account for scr refresh
            text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text1.started')
            # update status
            text1.status = STARTED
            text1.setAutoDraw(True)
        
        # if text1 is active this frame...
        if text1.status == STARTED:
            # update params
            pass
        
        # *key_resp1* updates
        waitOnFlip = False
        
        # if key_resp1 is starting this frame...
        if key_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp1.frameNStart = frameN  # exact frame index
            key_resp1.tStart = t  # local t and not account for scr refresh
            key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp1.started')
            # update status
            key_resp1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp1_allKeys.extend(theseKeys)
            if len(_key_resp1_allKeys):
                key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                key_resp1.rt = _key_resp1_allKeys[-1].rt
                key_resp1.duration = _key_resp1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=start,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            start.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if start.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in start.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start" ---
    for thisComponent in start.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start
    start.tStop = globalClock.getTime(format='float')
    start.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start.stopped', start.tStop)
    # check responses
    if key_resp1.keys in ['', [], None]:  # No response was made
        key_resp1.keys = None
    thisExp.addData('key_resp1.keys',key_resp1.keys)
    if key_resp1.keys != None:  # we had a response
        thisExp.addData('key_resp1.rt', key_resp1.rt)
        thisExp.addData('key_resp1.duration', key_resp1.duration)
    thisExp.nextEntry()
    # the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    sentencetrial = data.TrialHandler2(
        name='sentencetrial',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('TotalSentence.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(sentencetrial)  # add the loop to the experiment
    thisSentencetrial = sentencetrial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSentencetrial.rgb)
    if thisSentencetrial != None:
        for paramName in thisSentencetrial:
            globals()[paramName] = thisSentencetrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisSentencetrial in sentencetrial:
        sentencetrial.status = STARTED
        if hasattr(thisSentencetrial, 'status'):
            thisSentencetrial.status = STARTED
        currentLoop = sentencetrial
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisSentencetrial.rgb)
        if thisSentencetrial != None:
            for paramName in thisSentencetrial:
                globals()[paramName] = thisSentencetrial[paramName]
        
        # set up handler to look after randomisation of conditions etc
        wordtrial = data.TrialHandler2(
            name='wordtrial',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(wordtrial)  # add the loop to the experiment
        thisWordtrial = wordtrial.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisWordtrial.rgb)
        if thisWordtrial != None:
            for paramName in thisWordtrial:
                globals()[paramName] = thisWordtrial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisWordtrial in wordtrial:
            wordtrial.status = STARTED
            if hasattr(thisWordtrial, 'status'):
                thisWordtrial.status = STARTED
            currentLoop = wordtrial
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisWordtrial.rgb)
            if thisWordtrial != None:
                for paramName in thisWordtrial:
                    globals()[paramName] = thisWordtrial[paramName]
            
            # --- Prepare to start Routine "Loop" ---
            # create an object to store info about Routine Loop
            Loop = data.Routine(
                name='Loop',
                components=[shown_stim, response_instr, end_instr, tmp, underline, underline_hint, textbox],
            )
            Loop.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            cur_word_idx = 0
            endClock = core.Clock()
            need_end=0
            word_onset = 0
            participant_num = int(expInfo['participant_number'])
            if participant_num % 4 == 1 or participant_num % 4 == 0:
                words = sentencetrial.thisTrial['sentence1'].split()
            else:
                words = sentencetrial.thisTrial['sentence2'].split()
            textbox.reset()
            # store start times for Loop
            Loop.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Loop.tStart = globalClock.getTime(format='float')
            Loop.status = STARTED
            thisExp.addData('Loop.started', Loop.tStart)
            Loop.maxDuration = None
            # keep track of which components have finished
            LoopComponents = Loop.components
            for thisComponent in Loop.components:
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
            
            # --- Run Routine "Loop" ---
            thisExp.currentRoutine = Loop
            Loop.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisWordtrial, 'status') and thisWordtrial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code
                shown = ' '.join(words[:cur_word_idx+1])
                shown_stim.text = shown
                next_phrase = ' '.join(words[cur_word_idx+1:])
                tmp.text = next_phrase
                shown_stim.draw()
                continueRoutine = True
                if cur_word_idx == 0:
                    word_onset = globalClock.getTime()
                if cur_word_idx < len(words)-1 :
                    #set underline_hint
                    char_width_estimate = 0.044
                    remaining_width = len(next_phrase) * char_width_estimate
                    shown_width = len(shown) * char_width_estimate
                    offset = cur_word_idx * 0.015
                    start_x = -0.67 - offset
                    x_center = start_x + shown_width + remaining_width/2 - 0.044
                    shown_stim_center = start_x + shown_width/2
                    shown_stim.pos = (shown_stim_center, 0.33)
                    underline_hint.size = (remaining_width*3, 0)
                    underline_hint.pos = (x_center, 0.3)
                    
                    keys = event.getKeys(keyList=['return'])
                    response_instr.draw()
                    underline_hint.draw()
                    underline.draw()
                    textbox.draw()
                    continueRoutine = True
                    if keys and 'return' in keys:
                        if textbox.text != '':
                            #data collection
                            typed_text = textbox.getText() if hasattr(textbox, 'getText') else textbox.text
                            thisExp.addData('word_i', cur_word_idx)
                            thisExp.addData('word', words[cur_word_idx])
                            thisExp.addData('typed', typed_text)
                            thisExp.addData('RT', globalClock.getTime() - word_onset)
                            thisExp.nextEntry()
                            
                            textbox.setText('')
                            cur_word_idx += 1
                            shown = ' '.join(words[:cur_word_idx+1])
                            word_onset = globalClock.getTime()
                            shown_stim.draw()
                            endClock.reset()
                            continueRoutine = True
                elif cur_word_idx >= len(words) - 1 :
                    need_end=1
                    end_instr.draw()
                    #shown_stim_center = start_x + shown_width / 2 + len(words[cur_word_idx]) * 0.05
                    shown_stim.pos = (0, 0.33)
                    shown_stim.draw()
                    continueRoutine = True
                    if endClock.getTime() >= 2.0:
                        continueRoutine = False
                
                # *shown_stim* updates
                
                # if shown_stim is starting this frame...
                if shown_stim.status == NOT_STARTED and 0.0:
                    # keep track of start time/frame for later
                    shown_stim.frameNStart = frameN  # exact frame index
                    shown_stim.tStart = t  # local t and not account for scr refresh
                    shown_stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(shown_stim, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'shown_stim.started')
                    # update status
                    shown_stim.status = STARTED
                    shown_stim.setAutoDraw(True)
                
                # if shown_stim is active this frame...
                if shown_stim.status == STARTED:
                    # update params
                    pass
                
                # *response_instr* updates
                
                # if response_instr is starting this frame...
                if response_instr.status == NOT_STARTED and 0.0:
                    # keep track of start time/frame for later
                    response_instr.frameNStart = frameN  # exact frame index
                    response_instr.tStart = t  # local t and not account for scr refresh
                    response_instr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response_instr, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response_instr.started')
                    # update status
                    response_instr.status = STARTED
                    response_instr.setAutoDraw(True)
                
                # if response_instr is active this frame...
                if response_instr.status == STARTED:
                    # update params
                    pass
                
                # if response_instr is stopping this frame...
                if response_instr.status == STARTED:
                    if bool(need_end):
                        # keep track of stop time/frame for later
                        response_instr.tStop = t  # not accounting for scr refresh
                        response_instr.tStopRefresh = tThisFlipGlobal  # on global time
                        response_instr.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response_instr.stopped')
                        # update status
                        response_instr.status = FINISHED
                        response_instr.setAutoDraw(False)
                
                # *end_instr* updates
                
                # if end_instr is starting this frame...
                if end_instr.status == NOT_STARTED and need_end:
                    # keep track of start time/frame for later
                    end_instr.frameNStart = frameN  # exact frame index
                    end_instr.tStart = t  # local t and not account for scr refresh
                    end_instr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(end_instr, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'end_instr.started')
                    # update status
                    end_instr.status = STARTED
                    end_instr.setAutoDraw(True)
                
                # if end_instr is active this frame...
                if end_instr.status == STARTED:
                    # update params
                    pass
                
                # if end_instr is stopping this frame...
                if end_instr.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > end_instr.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        end_instr.tStop = t  # not accounting for scr refresh
                        end_instr.tStopRefresh = tThisFlipGlobal  # on global time
                        end_instr.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'end_instr.stopped')
                        # update status
                        end_instr.status = FINISHED
                        end_instr.setAutoDraw(False)
                
                # *tmp* updates
                
                # if tmp is starting this frame...
                if tmp.status == NOT_STARTED and 0.0:
                    # keep track of start time/frame for later
                    tmp.frameNStart = frameN  # exact frame index
                    tmp.tStart = t  # local t and not account for scr refresh
                    tmp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(tmp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tmp.started')
                    # update status
                    tmp.status = STARTED
                    tmp.setAutoDraw(True)
                
                # if tmp is active this frame...
                if tmp.status == STARTED:
                    # update params
                    pass
                
                # *underline* updates
                
                # if underline is starting this frame...
                if underline.status == NOT_STARTED and 0.0:
                    # keep track of start time/frame for later
                    underline.frameNStart = frameN  # exact frame index
                    underline.tStart = t  # local t and not account for scr refresh
                    underline.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(underline, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'underline.started')
                    # update status
                    underline.status = STARTED
                    underline.setAutoDraw(True)
                
                # if underline is active this frame...
                if underline.status == STARTED:
                    # update params
                    pass
                
                # if underline is stopping this frame...
                if underline.status == STARTED:
                    if bool(need_end):
                        # keep track of stop time/frame for later
                        underline.tStop = t  # not accounting for scr refresh
                        underline.tStopRefresh = tThisFlipGlobal  # on global time
                        underline.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'underline.stopped')
                        # update status
                        underline.status = FINISHED
                        underline.setAutoDraw(False)
                
                # *underline_hint* updates
                
                # if underline_hint is starting this frame...
                if underline_hint.status == NOT_STARTED and 0.0:
                    # keep track of start time/frame for later
                    underline_hint.frameNStart = frameN  # exact frame index
                    underline_hint.tStart = t  # local t and not account for scr refresh
                    underline_hint.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(underline_hint, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'underline_hint.started')
                    # update status
                    underline_hint.status = STARTED
                    underline_hint.setAutoDraw(True)
                
                # if underline_hint is active this frame...
                if underline_hint.status == STARTED:
                    # update params
                    pass
                
                # if underline_hint is stopping this frame...
                if underline_hint.status == STARTED:
                    if bool(need_end):
                        # keep track of stop time/frame for later
                        underline_hint.tStop = t  # not accounting for scr refresh
                        underline_hint.tStopRefresh = tThisFlipGlobal  # on global time
                        underline_hint.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'underline_hint.stopped')
                        # update status
                        underline_hint.status = FINISHED
                        underline_hint.setAutoDraw(False)
                
                # *textbox* updates
                
                # if textbox is active this frame...
                if textbox.status == STARTED:
                    # update params
                    pass
                
                # if textbox is stopping this frame...
                if textbox.status == STARTED:
                    if bool(need_end):
                        # keep track of stop time/frame for later
                        textbox.tStop = t  # not accounting for scr refresh
                        textbox.tStopRefresh = tThisFlipGlobal  # on global time
                        textbox.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox.stopped')
                        # update status
                        textbox.status = FINISHED
                        textbox.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=Loop,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    Loop.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if Loop.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in Loop.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Loop" ---
            for thisComponent in Loop.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Loop
            Loop.tStop = globalClock.getTime(format='float')
            Loop.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Loop.stopped', Loop.tStop)
            wordtrial.addData('textbox.text',textbox.text)
            # the Routine "Loop" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisWordtrial as finished
            if hasattr(thisWordtrial, 'status'):
                thisWordtrial.status = FINISHED
            # if awaiting a pause, pause now
            if wordtrial.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                wordtrial.status = STARTED
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'wordtrial'
        wordtrial.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # mark thisSentencetrial as finished
        if hasattr(thisSentencetrial, 'status'):
            thisSentencetrial.status = FINISHED
        # if awaiting a pause, pause now
        if sentencetrial.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            sentencetrial.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'sentencetrial'
    sentencetrial.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[endword],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
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
    thisExp.currentRoutine = end
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endword* updates
        
        # if endword is starting this frame...
        if endword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endword.frameNStart = frameN  # exact frame index
            endword.tStart = t  # local t and not account for scr refresh
            endword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endword.started')
            # update status
            endword.status = STARTED
            endword.setAutoDraw(True)
        
        # if endword is active this frame...
        if endword.status == STARTED:
            # update params
            pass
        
        # if endword is stopping this frame...
        if endword.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endword.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                endword.tStop = t  # not accounting for scr refresh
                endword.tStopRefresh = tThisFlipGlobal  # on global time
                endword.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'endword.stopped')
                # update status
                endword.status = FINISHED
                endword.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=end,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            end.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if end.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end.maxDurationReached:
        routineTimer.addTime(-end.maxDuration)
    elif end.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


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


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
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
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
