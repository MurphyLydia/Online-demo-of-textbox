/*************************************** 
 * Onlinedemo_English_Instruction *
 ***************************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.2.0.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'OnlineDemo_english_instruction';  // from the Builder filename that created this script
let expInfo = {
    'participant_number': '',
    'gender': '',
    'age': '',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(startRoutineBegin());
flowScheduler.add(startRoutineEachFrame());
flowScheduler.add(startRoutineEnd());
const sentencetrialLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(sentencetrialLoopBegin(sentencetrialLoopScheduler));
flowScheduler.add(sentencetrialLoopScheduler);
flowScheduler.add(sentencetrialLoopEnd);




flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'TotalSentence.xlsx', 'path': 'TotalSentence.xlsx'},
    {'name': 'TotalSentence.xlsx', 'path': 'TotalSentence.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.2.0';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant_number"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var startClock;
var text1;
var key_resp1;
var LoopClock;
var firstKeyClock;
var hasFirstKey;
var shown_stim;
var response_instr;
var end_instr;
var tmp;
var underline;
var underline_hint;
var textbox;
var endClock;
var endword;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "start"
  startClock = new util.Clock();
  text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text1',
    text: 'In this experiment, based on the given sentence sequence, \nplease type the word that is expected to appear next. \nExample:\n提示された語列1：「今日は」\n→ タイプ例：「天気が」\n\n提示された語列2：「今日は天気が」\n→ タイプ例：「いいです」\n\nThere are no correct or incorrect answers for the input words.\nPlease input the word that comes to mind based on your first impression.\nThe length of the content is not limited.\nAfter typing the single word, please press the Enter/Return key.\nThis experiment consists of a total of 60 sentences.\nIn a quiet environment, please conduct the experiment\nindependently without seeking help from others.\nWhen you are ready, press the SPACE to start the experiment.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Loop"
  LoopClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  firstKeyClock = new util.Clock();
  hasFirstKey = false;
  
  shown_stim = new visual.TextStim({
    win: psychoJS.window,
    name: 'shown_stim',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.8), 0.37], draggable: false, height: 0.044,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  response_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'response_instr',
    text: 'Type the next words:',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), (- 0.185)], draggable: false, height: 0.044,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  end_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_instr',
    text: "That\\'s the end of sentence\nNext sentence would appear after 2s",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.185)], draggable: false, height: 0.05,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  tmp = new visual.TextStim({
    win: psychoJS.window,
    name: 'tmp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.8), 0], draggable: false, height: 0.044,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  underline = new visual.ShapeStim ({
    win: psychoJS.window, name: 'underline', 
    vertices: [[-[0.4, 0][0]/2.0, 0], [+[0.4, 0][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0.2, (- 0.222)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -5, 
    interpolate: true, 
  });
  
  underline_hint = new visual.ShapeStim ({
    win: psychoJS.window, name: 'underline_hint', 
    vertices: [[-[0.3, 0.0][0]/2.0, 0], [+[0.3, 0.0][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, 0.3], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -6, 
    interpolate: true, 
  });
  
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    placeholder: undefined,
    font: 'SimSun',
    pos: [0.2, (- 0.185)], 
    draggable: false,
    letterHeight: 0.044,
    lineSpacing: 1.0,
    size: [0.5, 0.0556],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -7.0 
  });
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  endword = new visual.TextStim({
    win: psychoJS.window,
    name: 'endword',
    text: "That\\'s the end of experiment.\nThis program would close automatically after 2s.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var startMaxDurationReached;
var _key_resp1_allKeys;
var startMaxDuration;
var startComponents;
function startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    startClock.reset();
    routineTimer.reset();
    startMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp1.keys = undefined;
    key_resp1.rt = undefined;
    _key_resp1_allKeys = [];
    psychoJS.experiment.addData('start.started', globalClock.getTime());
    startMaxDuration = null
    // keep track of which components have finished
    startComponents = [];
    startComponents.push(text1);
    startComponents.push(key_resp1);
    
    for (const thisComponent of startComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function startRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start' ---
    // get current time
    t = startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text1* updates
    if (t >= 0.0 && text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text1.tStart = t;  // (not accounting for frame time here)
      text1.frameNStart = frameN;  // exact frame index
      
      text1.setAutoDraw(true);
    }
    
    
    // if text1 is active this frame...
    if (text1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp1* updates
    if (t >= 0.0 && key_resp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp1.tStart = t;  // (not accounting for frame time here)
      key_resp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp1.clearEvents(); });
    }
    
    // if key_resp1 is active this frame...
    if (key_resp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp1.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_resp1_allKeys = _key_resp1_allKeys.concat(theseKeys);
      if (_key_resp1_allKeys.length > 0) {
        key_resp1.keys = _key_resp1_allKeys[_key_resp1_allKeys.length - 1].name;  // just the last key pressed
        key_resp1.rt = _key_resp1_allKeys[_key_resp1_allKeys.length - 1].rt;
        key_resp1.duration = _key_resp1_allKeys[_key_resp1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start' ---
    for (const thisComponent of startComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('start.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp1.corr, level);
    }
    psychoJS.experiment.addData('key_resp1.keys', key_resp1.keys);
    if (typeof key_resp1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp1.rt', key_resp1.rt);
        psychoJS.experiment.addData('key_resp1.duration', key_resp1.duration);
        routineTimer.reset();
        }
    
    key_resp1.stop();
    // the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var sentencetrial;
function sentencetrialLoopBegin(sentencetrialLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    sentencetrial = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TotalSentence.xlsx',
      seed: undefined, name: 'sentencetrial'
    });
    psychoJS.experiment.addLoop(sentencetrial); // add the loop to the experiment
    currentLoop = sentencetrial;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSentencetrial of sentencetrial) {
      snapshot = sentencetrial.getSnapshot();
      sentencetrialLoopScheduler.add(importConditions(snapshot));
      const wordtrialLoopScheduler = new Scheduler(psychoJS);
      sentencetrialLoopScheduler.add(wordtrialLoopBegin(wordtrialLoopScheduler, snapshot));
      sentencetrialLoopScheduler.add(wordtrialLoopScheduler);
      sentencetrialLoopScheduler.add(wordtrialLoopEnd);
      sentencetrialLoopScheduler.add(sentencetrialLoopEndIteration(sentencetrialLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var wordtrial;
function wordtrialLoopBegin(wordtrialLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    wordtrial = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'wordtrial'
    });
    psychoJS.experiment.addLoop(wordtrial); // add the loop to the experiment
    currentLoop = wordtrial;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisWordtrial of wordtrial) {
      snapshot = wordtrial.getSnapshot();
      wordtrialLoopScheduler.add(importConditions(snapshot));
      wordtrialLoopScheduler.add(LoopRoutineBegin(snapshot));
      wordtrialLoopScheduler.add(LoopRoutineEachFrame());
      wordtrialLoopScheduler.add(LoopRoutineEnd(snapshot));
      wordtrialLoopScheduler.add(wordtrialLoopEndIteration(wordtrialLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function wordtrialLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(wordtrial);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function wordtrialLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function sentencetrialLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(sentencetrial);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function sentencetrialLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var LoopMaxDurationReached;
var cur_word_idx;
var need_end;
var word_onset;
var participant_num;
var words;
var LoopMaxDuration;
var LoopComponents;
function LoopRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Loop' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    LoopClock.reset();
    routineTimer.reset();
    LoopMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    cur_word_idx = 0;
    endClock = new util.Clock();
    need_end = 0;
    word_onset = 0;
    participant_num = Number.parseInt(expInfo["participant_number"]);
    if ((((participant_num % 4) === 1) || ((participant_num % 4) === 0))) {
        words = sentencetrial.thisTrial["sentence1"].split(" ");
    } else {
        words = sentencetrial.thisTrial["sentence2"].split(" ");
    }
    
    textbox.setText('');
    textbox.refresh();
    psychoJS.experiment.addData('Loop.started', globalClock.getTime());
    LoopMaxDuration = null
    // keep track of which components have finished
    LoopComponents = [];
    LoopComponents.push(shown_stim);
    LoopComponents.push(response_instr);
    LoopComponents.push(end_instr);
    LoopComponents.push(tmp);
    LoopComponents.push(underline);
    LoopComponents.push(underline_hint);
    LoopComponents.push(textbox);
    
    for (const thisComponent of LoopComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var shown;
var next_phrase;
var char_width_estimate;
var remaining_width;
var shown_width;
var offset;
var start_x;
var x_center;
var shown_stim_center;
var keys;
var typed_text;
function LoopRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Loop' ---
    // get current time
    t = LoopClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    shown = words.slice(0, (cur_word_idx + 1)).join(" ");
    shown_stim.text = shown;
    next_phrase = words.slice((cur_word_idx + 1)).join(" ");
    tmp.text = next_phrase;
    shown_stim.draw();
    continueRoutine = true;
    if ((cur_word_idx === 0)) {
        word_onset = globalClock.getTime();
    }
    if ((cur_word_idx < (words.length - 1))) {
        char_width_estimate = 0.044;
        remaining_width = (next_phrase.length * char_width_estimate);
        shown_width = (shown.length * char_width_estimate);
        offset = (cur_word_idx * 0.015);
        start_x = ((- 0.67) - offset);
        x_center = (((start_x + shown_width) + (remaining_width / 2)) - 0.044);
        shown_stim_center = (start_x + (shown_width / 2));
        shown_stim.pos = [shown_stim_center, 0.33];
        underline_hint.size = [(remaining_width * 3), 0];
        underline_hint.pos = [x_center, 0.3];
        keys = psychoJS.eventManager.getKeys({"keyList": ["return"]});
        response_instr.draw();
        underline_hint.draw();
        underline.draw();
        textbox.draw();
        continueRoutine = true;
        if ((keys && _pj.in_es6("return", keys))) {
            if ((textbox.text !== "")) {
                typed_text = (("getText" in textbox) ? textbox.getText() : textbox.text);
                psychoJS.experiment.addData("word_i", cur_word_idx);
                psychoJS.experiment.addData("word", words[cur_word_idx]);
                psychoJS.experiment.addData("typed", typed_text);
                psychoJS.experiment.addData("RT", (globalClock.getTime() - word_onset));
                psychoJS.experiment.nextEntry();
                textbox.setText("");
                cur_word_idx += 1;
                shown = words.slice(0, (cur_word_idx + 1)).join(" ");
                word_onset = globalClock.getTime();
                shown_stim.draw();
                endClock.reset();
                continueRoutine = true;
            }
        }
    } else {
        if ((cur_word_idx >= (words.length - 1))) {
            need_end = 1;
            end_instr.draw();
            shown_stim.pos = [0, 0.33];
            shown_stim.draw();
            continueRoutine = true;
            if ((endClock.getTime() >= 2.0)) {
                continueRoutine = false;
            }
        }
    }
    
    
    // *shown_stim* updates
    if ((0.0) && shown_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shown_stim.tStart = t;  // (not accounting for frame time here)
      shown_stim.frameNStart = frameN;  // exact frame index
      
      shown_stim.setAutoDraw(true);
    }
    
    
    // if shown_stim is active this frame...
    if (shown_stim.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *response_instr* updates
    if ((0.0) && response_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_instr.tStart = t;  // (not accounting for frame time here)
      response_instr.frameNStart = frameN;  // exact frame index
      
      response_instr.setAutoDraw(true);
    }
    
    
    // if response_instr is active this frame...
    if (response_instr.status === PsychoJS.Status.STARTED) {
    }
    
    if (response_instr.status === PsychoJS.Status.STARTED && Boolean(need_end)) {
      // keep track of stop time/frame for later
      response_instr.tStop = t;  // not accounting for scr refresh
      response_instr.frameNStop = frameN;  // exact frame index
      // update status
      response_instr.status = PsychoJS.Status.FINISHED;
      response_instr.setAutoDraw(false);
    }
    
    
    // *end_instr* updates
    if ((need_end) && end_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_instr.tStart = t;  // (not accounting for frame time here)
      end_instr.frameNStart = frameN;  // exact frame index
      
      end_instr.setAutoDraw(true);
    }
    
    
    // if end_instr is active this frame...
    if (end_instr.status === PsychoJS.Status.STARTED) {
    }
    
    if (end_instr.status === PsychoJS.Status.STARTED && t >= (end_instr.tStart + 1.0)) {
      // keep track of stop time/frame for later
      end_instr.tStop = t;  // not accounting for scr refresh
      end_instr.frameNStop = frameN;  // exact frame index
      // update status
      end_instr.status = PsychoJS.Status.FINISHED;
      end_instr.setAutoDraw(false);
    }
    
    
    // *tmp* updates
    if ((0.0) && tmp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tmp.tStart = t;  // (not accounting for frame time here)
      tmp.frameNStart = frameN;  // exact frame index
      
      tmp.setAutoDraw(true);
    }
    
    
    // if tmp is active this frame...
    if (tmp.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *underline* updates
    if ((0.0) && underline.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      underline.tStart = t;  // (not accounting for frame time here)
      underline.frameNStart = frameN;  // exact frame index
      
      underline.setAutoDraw(true);
    }
    
    
    // if underline is active this frame...
    if (underline.status === PsychoJS.Status.STARTED) {
    }
    
    if (underline.status === PsychoJS.Status.STARTED && Boolean(need_end)) {
      // keep track of stop time/frame for later
      underline.tStop = t;  // not accounting for scr refresh
      underline.frameNStop = frameN;  // exact frame index
      // update status
      underline.status = PsychoJS.Status.FINISHED;
      underline.setAutoDraw(false);
    }
    
    
    // *underline_hint* updates
    if ((0.0) && underline_hint.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      underline_hint.tStart = t;  // (not accounting for frame time here)
      underline_hint.frameNStart = frameN;  // exact frame index
      
      underline_hint.setAutoDraw(true);
    }
    
    
    // if underline_hint is active this frame...
    if (underline_hint.status === PsychoJS.Status.STARTED) {
    }
    
    if (underline_hint.status === PsychoJS.Status.STARTED && Boolean(need_end)) {
      // keep track of stop time/frame for later
      underline_hint.tStop = t;  // not accounting for scr refresh
      underline_hint.frameNStop = frameN;  // exact frame index
      // update status
      underline_hint.status = PsychoJS.Status.FINISHED;
      underline_hint.setAutoDraw(false);
    }
    
    
    // *textbox* updates
    
    // if textbox is active this frame...
    if (textbox.status === PsychoJS.Status.STARTED) {
    }
    
    if (textbox.status === PsychoJS.Status.STARTED && Boolean(need_end)) {
      // keep track of stop time/frame for later
      textbox.tStop = t;  // not accounting for scr refresh
      textbox.frameNStop = frameN;  // exact frame index
      // update status
      textbox.status = PsychoJS.Status.FINISHED;
      textbox.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LoopComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LoopRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Loop' ---
    for (const thisComponent of LoopComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Loop.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox.text',textbox.text)
    // the Routine "Loop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endMaxDurationReached;
var endMaxDuration;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    endClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    endMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    endMaxDuration = null
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(endword);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endword* updates
    if (t >= 0.0 && endword.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endword.tStart = t;  // (not accounting for frame time here)
      endword.frameNStart = frameN;  // exact frame index
      
      endword.setAutoDraw(true);
    }
    
    
    // if endword is active this frame...
    if (endword.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (endword.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      endword.tStop = t;  // not accounting for scr refresh
      endword.frameNStop = frameN;  // exact frame index
      // update status
      endword.status = PsychoJS.Status.FINISHED;
      endword.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (endMaxDurationReached) {
        endClock.add(endMaxDuration);
    } else {
        endClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
