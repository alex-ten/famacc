/******************* 
 * Confidence *
 *******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'confidence';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code_wordlist
let word_list = ['psythos','addaign', 'gyepset', 'oppasms','ridaps','sclueeze', 
'addlaim'];
util.shuffle(word_list)

let rep_times = [1,2,3,4,5,5,7];
util.shuffle(rep_times)

let WW = [];
let W_train = [];

for (let i = 0; i < word_list.length; i++) {
  for (let j = 0; j < rep_times[i]; j++) {
    WW.push(word_list[i]);
    W_train.push(word_list[i]);
  }
}

let combined = WW.map((item, i) => [item, W_train[i]]);
util.shuffle(combined)

WW = combined.map(item => item[0]);
W_train = combined.map(item => item[1]);

let len_W_train = W_train.length;  

//----------------------------

let psuedo_lists = [];
let list_size = 3;         


let num_new_lists = Math.floor(WW.length / list_size);


while (WW.length >= list_size+5) {
    let first_elem = WW.splice(Math.floor(Math.random()*WW.length), 1)[0];
    
    let second_elem = WW.splice(Math.floor(Math.random()*WW.length), 1)[0];
    while (second_elem === first_elem) {
        second_elem = WW.splice(Math.floor(Math.random()*WW.length), 1)[0];
    }
    let third_elem = WW.splice(Math.floor(Math.random()*WW.length), 1)[0];
    while (third_elem === first_elem || third_elem===second_elem) {
        third_elem = WW.splice(Math.floor(Math.random()*WW.length), 1)[0];
    }
    
    psuedo_lists.push([first_elem, second_elem,third_elem]);
    }

let len_trials = psuedo_lists.length; 
let len_assoc_trials = word_list.length;

console.log(psuedo_lists);

// Run 'Before Experiment' code from code
let feature1 = ["Red", "Blue", "Green", "Yellow", "Orange", "Pink", 
"Black"];

util.shuffle(feature1)

let feature2 = [1, 2, 3, 4, 5, 6, 7];
util.shuffle(feature2)

let feature3 = ["e", "f", "g", "h", "i", "j", "k"];
util.shuffle(feature3)

let feature4 = ['!', '@', '#', '$', '%', '^', '&'];
util.shuffle(feature4)

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
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
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);



const loop_trainLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop_trainLoopBegin(loop_trainLoopScheduler));
flowScheduler.add(loop_trainLoopScheduler);
flowScheduler.add(loop_trainLoopEnd);


flowScheduler.add(test_InstructRoutineBegin());
flowScheduler.add(test_InstructRoutineEachFrame());
flowScheduler.add(test_InstructRoutineEnd());
const loop_testLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop_testLoopBegin(loop_testLoopScheduler));
flowScheduler.add(loop_testLoopScheduler);
flowScheduler.add(loop_testLoopEnd);



flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var InstructionsClock;
var text_Welcome;
var text_Instructions;
var key_resp_complete;
var psuedowordsClock;
var iter;
var text_psuedoword1;
var text_psuedoword2;
var text_psuedoword3;
var text_delay;
var memoryClock;
var text_instruct_memory;
var textbox_word1;
var textbox_word2;
var textbox_word3;
var button;
var text_button;
var trainClock;
var iter_train;
var text_psuedowords;
var text_f1;
var text_f2;
var text_f3;
var text_f4;
var test_InstructClock;
var text_Inst;
var testClock;
var iter_test;
var text_test;
var textbox_f1;
var textbox_f2;
var textbox_f3;
var textbox_f4;
var button_2;
var text_button_2;
var delayClock;
var text;
var endClock;
var text_end;
var key_resp_end;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  text_Welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Welcome',
    text: 'Welcome',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_Instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Instructions',
    text: 'Instructions\n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_complete = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "psuedowords"
  psuedowordsClock = new util.Clock();
  // Run 'Begin Experiment' code from code_wordlist
  iter = (- 1);
  
  
  text_psuedoword1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_psuedoword1',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_psuedoword2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_psuedoword2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_psuedoword3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_psuedoword3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_delay = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_delay',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "memory"
  memoryClock = new util.Clock();
  text_instruct_memory = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_instruct_memory',
    text: 'Write down the words you just saw',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textbox_word1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_word1',
    text: '',
    placeholder: 'Type the first word here...',
    font: 'Arial',
    pos: [(- 0.5), 0], 
    letterHeight: 0.04,
    lineSpacing: 0.5,
    size: [0.3, 0.3],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  textbox_word2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_word2',
    text: '',
    placeholder: 'Type second word here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.04,
    lineSpacing: 0.5,
    size: [0.3, 0.3],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  textbox_word3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_word3',
    text: '',
    placeholder: 'Type second word here...',
    font: 'Arial',
    pos: [0.5, 0], 
    letterHeight: 0.04,
    lineSpacing: 0.5,
    size: [0.3, 0.3],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  button = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button',
    text: 'Done',
    fillColor: 'darkgray',
    borderColor: [0.0, 0.0, 0.0],
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.5, (- 0.4)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    depth: -4
  });
  button.clock = new util.Clock();
  
  text_button = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_button',
    text: 'Done',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "train"
  trainClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  iter_train = (- 1);
  
  text_psuedowords = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_psuedowords',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_f1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_f1',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.5), 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_f2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_f2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_f3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_f3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  text_f4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_f4',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "test_Instruct"
  test_InstructClock = new util.Clock();
  text_Inst = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Inst',
    text: 'Write down the features associated with these words',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "test"
  testClock = new util.Clock();
  // Run 'Begin Experiment' code from code_test
  iter_test = (- 1);
  
  text_test = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_test',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  textbox_f1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_f1',
    text: '',
    placeholder: 'feature 1',
    font: 'Arial',
    pos: [(- 0.55), 0], 
    letterHeight: 0.04,
    lineSpacing: 0.5,
    size: [0.3, 0.3],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  textbox_f2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_f2',
    text: '',
    placeholder: 'feature 2',
    font: 'Arial',
    pos: [(- 0.2), 0], 
    letterHeight: 0.04,
    lineSpacing: 0.5,
    size: [0.3, 0.3],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  textbox_f3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_f3',
    text: '',
    placeholder: 'feature 3',
    font: 'Arial',
    pos: [0.2, 0], 
    letterHeight: 0.04,
    lineSpacing: 0.5,
    size: [0.3, 0.3],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  textbox_f4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_f4',
    text: '',
    placeholder: 'feature 4',
    font: 'Arial',
    pos: [0.55, 0], 
    letterHeight: 0.04,
    lineSpacing: 0.5,
    size: [0.3, 0.3],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  button_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_2',
    text: 'Done',
    fillColor: 'darkgray',
    borderColor: [0.0, 0.0, 0.0],
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.5, (- 0.4)],
    letterHeight: 0.05,
    size: [0.2, 0.2],
    depth: -6
  });
  button_2.clock = new util.Clock();
  
  text_button_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_button_2',
    text: 'Done',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "delay"
  delayClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text_end = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_end',
    text: 'Finished\n\nPress SPACE to end.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_end = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_complete_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instructions.started', globalClock.getTime());
    key_resp_complete.keys = undefined;
    key_resp_complete.rt = undefined;
    _key_resp_complete_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(text_Welcome);
    InstructionsComponents.push(text_Instructions);
    InstructionsComponents.push(key_resp_complete);
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Welcome* updates
    if (t >= 0.0 && text_Welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Welcome.tStart = t;  // (not accounting for frame time here)
      text_Welcome.frameNStart = frameN;  // exact frame index
      
      text_Welcome.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_Welcome.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_Welcome.setAutoDraw(false);
    }
    
    // *text_Instructions* updates
    if (t >= 1 && text_Instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Instructions.tStart = t;  // (not accounting for frame time here)
      text_Instructions.frameNStart = frameN;  // exact frame index
      
      text_Instructions.setAutoDraw(true);
    }
    
    
    // *key_resp_complete* updates
    if (t >= 2.0 && key_resp_complete.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_complete.tStart = t;  // (not accounting for frame time here)
      key_resp_complete.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_complete.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_complete.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_complete.clearEvents(); });
    }
    
    if (key_resp_complete.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_complete.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_complete_allKeys = _key_resp_complete_allKeys.concat(theseKeys);
      if (_key_resp_complete_allKeys.length > 0) {
        key_resp_complete.keys = _key_resp_complete_allKeys[_key_resp_complete_allKeys.length - 1].name;  // just the last key pressed
        key_resp_complete.rt = _key_resp_complete_allKeys[_key_resp_complete_allKeys.length - 1].rt;
        key_resp_complete.duration = _key_resp_complete_allKeys[_key_resp_complete_allKeys.length - 1].duration;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
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


function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_complete.corr, level);
    }
    psychoJS.experiment.addData('key_resp_complete.keys', key_resp_complete.keys);
    if (typeof key_resp_complete.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_complete.rt', key_resp_complete.rt);
        psychoJS.experiment.addData('key_resp_complete.duration', key_resp_complete.duration);
        routineTimer.reset();
        }
    
    key_resp_complete.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: len_trials, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(psuedowordsRoutineBegin(snapshot));
      trialsLoopScheduler.add(psuedowordsRoutineEachFrame());
      trialsLoopScheduler.add(psuedowordsRoutineEnd(snapshot));
      trialsLoopScheduler.add(memoryRoutineBegin(snapshot));
      trialsLoopScheduler.add(memoryRoutineEachFrame());
      trialsLoopScheduler.add(memoryRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
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


var loop_train;
function loop_trainLoopBegin(loop_trainLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_train = new TrialHandler({
      psychoJS: psychoJS,
      nReps: len_assoc_trials, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loop_train'
    });
    psychoJS.experiment.addLoop(loop_train); // add the loop to the experiment
    currentLoop = loop_train;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_train of loop_train) {
      snapshot = loop_train.getSnapshot();
      loop_trainLoopScheduler.add(importConditions(snapshot));
      loop_trainLoopScheduler.add(trainRoutineBegin(snapshot));
      loop_trainLoopScheduler.add(trainRoutineEachFrame());
      loop_trainLoopScheduler.add(trainRoutineEnd(snapshot));
      loop_trainLoopScheduler.add(loop_trainLoopEndIteration(loop_trainLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_trainLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_train);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_trainLoopEndIteration(scheduler, snapshot) {
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


var loop_test;
function loop_testLoopBegin(loop_testLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_test = new TrialHandler({
      psychoJS: psychoJS,
      nReps: len_assoc_trials, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loop_test'
    });
    psychoJS.experiment.addLoop(loop_test); // add the loop to the experiment
    currentLoop = loop_test;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop_test of loop_test) {
      snapshot = loop_test.getSnapshot();
      loop_testLoopScheduler.add(importConditions(snapshot));
      loop_testLoopScheduler.add(testRoutineBegin(snapshot));
      loop_testLoopScheduler.add(testRoutineEachFrame());
      loop_testLoopScheduler.add(testRoutineEnd(snapshot));
      loop_testLoopScheduler.add(delayRoutineBegin(snapshot));
      loop_testLoopScheduler.add(delayRoutineEachFrame());
      loop_testLoopScheduler.add(delayRoutineEnd(snapshot));
      loop_testLoopScheduler.add(loop_testLoopEndIteration(loop_testLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_testLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_test);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_testLoopEndIteration(scheduler, snapshot) {
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


var psuedowordsComponents;
function psuedowordsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'psuedowords' ---
    t = 0;
    psuedowordsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('psuedowords.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_wordlist
    // store the trial word list into separate words
    iter = (iter + 1);
    
    let psuedoword1 = psuedo_lists[iter][0];
    let psuedoword2 = psuedo_lists[iter][1];
    let psuedoword3 = psuedo_lists[iter][2];
    
    // store data
    psychoJS.experiment.addData("psuedoword1", psuedoword1);
    psychoJS.experiment.addData("psuedoword2", psuedoword2);
    psychoJS.experiment.addData("psuedoword3", psuedoword3);
    
    text_psuedoword1.setText(psuedoword1);
    text_psuedoword2.setText(psuedoword2);
    text_psuedoword3.setText(psuedoword3);
    // keep track of which components have finished
    psuedowordsComponents = [];
    psuedowordsComponents.push(text_psuedoword1);
    psuedowordsComponents.push(text_psuedoword2);
    psuedowordsComponents.push(text_psuedoword3);
    psuedowordsComponents.push(text_delay);
    
    for (const thisComponent of psuedowordsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function psuedowordsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'psuedowords' ---
    // get current time
    t = psuedowordsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_psuedoword1* updates
    if (t >= 0.0 && text_psuedoword1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_psuedoword1.tStart = t;  // (not accounting for frame time here)
      text_psuedoword1.frameNStart = frameN;  // exact frame index
      
      text_psuedoword1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_psuedoword1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_psuedoword1.setAutoDraw(false);
    }
    
    // *text_psuedoword2* updates
    if (t >= 0.5 && text_psuedoword2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_psuedoword2.tStart = t;  // (not accounting for frame time here)
      text_psuedoword2.frameNStart = frameN;  // exact frame index
      
      text_psuedoword2.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_psuedoword2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_psuedoword2.setAutoDraw(false);
    }
    
    // *text_psuedoword3* updates
    if (t >= 1 && text_psuedoword3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_psuedoword3.tStart = t;  // (not accounting for frame time here)
      text_psuedoword3.frameNStart = frameN;  // exact frame index
      
      text_psuedoword3.setAutoDraw(true);
    }
    
    frameRemains = 1 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_psuedoword3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_psuedoword3.setAutoDraw(false);
    }
    
    // *text_delay* updates
    if (t >= 1.5 && text_delay.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_delay.tStart = t;  // (not accounting for frame time here)
      text_delay.frameNStart = frameN;  // exact frame index
      
      text_delay.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_delay.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_delay.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of psuedowordsComponents)
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


function psuedowordsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'psuedowords' ---
    for (const thisComponent of psuedowordsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('psuedowords.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var memoryComponents;
function memoryRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'memory' ---
    t = 0;
    memoryClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('memory.started', globalClock.getTime());
    textbox_word1.setText('');
    textbox_word1.refresh();
    textbox_word1.setText('');
    textbox_word2.setText('');
    textbox_word2.refresh();
    textbox_word2.setText('');
    textbox_word3.setText('');
    textbox_word3.refresh();
    textbox_word3.setText('');
    // reset button to account for continued clicks & clear times on/off
    button.reset()
    // keep track of which components have finished
    memoryComponents = [];
    memoryComponents.push(text_instruct_memory);
    memoryComponents.push(textbox_word1);
    memoryComponents.push(textbox_word2);
    memoryComponents.push(textbox_word3);
    memoryComponents.push(button);
    memoryComponents.push(text_button);
    
    for (const thisComponent of memoryComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function memoryRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'memory' ---
    // get current time
    t = memoryClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_instruct_memory* updates
    if (t >= 0.0 && text_instruct_memory.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_instruct_memory.tStart = t;  // (not accounting for frame time here)
      text_instruct_memory.frameNStart = frameN;  // exact frame index
      
      text_instruct_memory.setAutoDraw(true);
    }
    
    
    // *textbox_word1* updates
    if (t >= 1.0 && textbox_word1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_word1.tStart = t;  // (not accounting for frame time here)
      textbox_word1.frameNStart = frameN;  // exact frame index
      
      textbox_word1.setAutoDraw(true);
    }
    
    
    // *textbox_word2* updates
    if (t >= 1.0 && textbox_word2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_word2.tStart = t;  // (not accounting for frame time here)
      textbox_word2.frameNStart = frameN;  // exact frame index
      
      textbox_word2.setAutoDraw(true);
    }
    
    
    // *textbox_word3* updates
    if (t >= 1.0 && textbox_word3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_word3.tStart = t;  // (not accounting for frame time here)
      textbox_word3.frameNStart = frameN;  // exact frame index
      
      textbox_word3.setAutoDraw(true);
    }
    
    
    // *button* updates
    if (t >= 0 && button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button.tStart = t;  // (not accounting for frame time here)
      button.frameNStart = frameN;  // exact frame index
      
      button.setAutoDraw(true);
    }
    
    if (button.status === PsychoJS.Status.STARTED) {
      // check whether button has been pressed
      if (button.isClicked) {
        if (!button.wasClicked) {
          // store time of first click
          button.timesOn.push(button.clock.getTime());
          button.numClicks += 1;
          // store time clicked until
          button.timesOff.push(button.clock.getTime());
        } else {
          // update time clicked until;
          button.timesOff[button.timesOff.length - 1] = button.clock.getTime();
        }
        if (!button.wasClicked) {
          // end routine when button is clicked
          continueRoutine = false;
          
        }
        // if button is still clicked next frame, it is not a new click
        button.wasClicked = true;
      } else {
        // if button is clicked next frame, it is a new click
        button.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button hasn't started / has finished
      button.clock.reset();
      // if button is clicked next frame, it is a new click
      button.wasClicked = false;
    }
    
    // *text_button* updates
    if (t >= 0.0 && text_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_button.tStart = t;  // (not accounting for frame time here)
      text_button.frameNStart = frameN;  // exact frame index
      
      text_button.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of memoryComponents)
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


function memoryRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'memory' ---
    for (const thisComponent of memoryComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('memory.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox_word1.text',textbox_word1.text)
    psychoJS.experiment.addData('textbox_word2.text',textbox_word2.text)
    psychoJS.experiment.addData('textbox_word3.text',textbox_word3.text)
    psychoJS.experiment.addData('button.numClicks', button.numClicks);
    psychoJS.experiment.addData('button.timesOn', button.timesOn);
    psychoJS.experiment.addData('button.timesOff', button.timesOff);
    // the Routine "memory" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trainComponents;
function trainRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'train' ---
    t = 0;
    trainClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('train.started', globalClock.getTime());
    // Run 'Begin Routine' code from code
    iter_train = (iter_train + 1);
    
    psychoJS.experiment.addData('psuedoword_train', word_list[iter_train]);
    psychoJS.experiment.addData('feature1', feature1[iter_train]);
    psychoJS.experiment.addData('feature2', feature2[iter_train]);
    psychoJS.experiment.addData('feature3', feature3[iter_train]);
    psychoJS.experiment.addData('feature4', feature4[iter_train]);
    text_psuedowords.setText(word_list[iter_train]);
    text_f1.setColor(new util.Color(feature1[iter_train]));
    text_f1.setText(feature1[iter_train]);
    text_f2.setText(feature2[iter_train]);
    text_f3.setText(feature3[iter_train]);
    text_f4.setText(feature4[iter_train]);
    // keep track of which components have finished
    trainComponents = [];
    trainComponents.push(text_psuedowords);
    trainComponents.push(text_f1);
    trainComponents.push(text_f2);
    trainComponents.push(text_f3);
    trainComponents.push(text_f4);
    
    for (const thisComponent of trainComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trainRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'train' ---
    // get current time
    t = trainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_psuedowords* updates
    if (t >= 0.0 && text_psuedowords.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_psuedowords.tStart = t;  // (not accounting for frame time here)
      text_psuedowords.frameNStart = frameN;  // exact frame index
      
      text_psuedowords.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_psuedowords.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_psuedowords.setAutoDraw(false);
    }
    
    // *text_f1* updates
    if (t >= 0.0 && text_f1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_f1.tStart = t;  // (not accounting for frame time here)
      text_f1.frameNStart = frameN;  // exact frame index
      
      text_f1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_f1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_f1.setAutoDraw(false);
    }
    
    // *text_f2* updates
    if (t >= 0.0 && text_f2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_f2.tStart = t;  // (not accounting for frame time here)
      text_f2.frameNStart = frameN;  // exact frame index
      
      text_f2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_f2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_f2.setAutoDraw(false);
    }
    
    // *text_f3* updates
    if (t >= 0.0 && text_f3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_f3.tStart = t;  // (not accounting for frame time here)
      text_f3.frameNStart = frameN;  // exact frame index
      
      text_f3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_f3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_f3.setAutoDraw(false);
    }
    
    // *text_f4* updates
    if (t >= 0.0 && text_f4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_f4.tStart = t;  // (not accounting for frame time here)
      text_f4.frameNStart = frameN;  // exact frame index
      
      text_f4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_f4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_f4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trainComponents)
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


function trainRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'train' ---
    for (const thisComponent of trainComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('train.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var test_InstructComponents;
function test_InstructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test_Instruct' ---
    t = 0;
    test_InstructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('test_Instruct.started', globalClock.getTime());
    // keep track of which components have finished
    test_InstructComponents = [];
    test_InstructComponents.push(text_Inst);
    
    for (const thisComponent of test_InstructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function test_InstructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test_Instruct' ---
    // get current time
    t = test_InstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Inst* updates
    if (t >= 0.0 && text_Inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Inst.tStart = t;  // (not accounting for frame time here)
      text_Inst.frameNStart = frameN;  // exact frame index
      
      text_Inst.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_Inst.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_Inst.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test_InstructComponents)
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


function test_InstructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test_Instruct' ---
    for (const thisComponent of test_InstructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test_Instruct.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var testComponents;
function testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test' ---
    t = 0;
    testClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('test.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_test
    iter_test = (iter_test + 1);
    
    psychoJS.experiment.addData("psuedoword_test", word_list[iter_test]);
    
    
    text_test.setText(word_list[iter_test]);
    textbox_f1.setText('');
    textbox_f1.refresh();
    textbox_f1.setText('');
    textbox_f2.setText('');
    textbox_f2.refresh();
    textbox_f2.setText('');
    textbox_f3.setText('');
    textbox_f3.refresh();
    textbox_f3.setText('');
    textbox_f4.setText('');
    textbox_f4.refresh();
    textbox_f4.setText('');
    // reset button_2 to account for continued clicks & clear times on/off
    button_2.reset()
    // keep track of which components have finished
    testComponents = [];
    testComponents.push(text_test);
    testComponents.push(textbox_f1);
    testComponents.push(textbox_f2);
    testComponents.push(textbox_f3);
    testComponents.push(textbox_f4);
    testComponents.push(button_2);
    testComponents.push(text_button_2);
    
    for (const thisComponent of testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test' ---
    // get current time
    t = testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_test* updates
    if (t >= 0.0 && text_test.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_test.tStart = t;  // (not accounting for frame time here)
      text_test.frameNStart = frameN;  // exact frame index
      
      text_test.setAutoDraw(true);
    }
    
    
    // *textbox_f1* updates
    if (t >= 0.5 && textbox_f1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_f1.tStart = t;  // (not accounting for frame time here)
      textbox_f1.frameNStart = frameN;  // exact frame index
      
      textbox_f1.setAutoDraw(true);
    }
    
    
    // *textbox_f2* updates
    if (t >= 0.5 && textbox_f2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_f2.tStart = t;  // (not accounting for frame time here)
      textbox_f2.frameNStart = frameN;  // exact frame index
      
      textbox_f2.setAutoDraw(true);
    }
    
    
    // *textbox_f3* updates
    if (t >= 0.5 && textbox_f3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_f3.tStart = t;  // (not accounting for frame time here)
      textbox_f3.frameNStart = frameN;  // exact frame index
      
      textbox_f3.setAutoDraw(true);
    }
    
    
    // *textbox_f4* updates
    if (t >= 0.5 && textbox_f4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_f4.tStart = t;  // (not accounting for frame time here)
      textbox_f4.frameNStart = frameN;  // exact frame index
      
      textbox_f4.setAutoDraw(true);
    }
    
    
    // *button_2* updates
    if (t >= 0 && button_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_2.tStart = t;  // (not accounting for frame time here)
      button_2.frameNStart = frameN;  // exact frame index
      
      button_2.setAutoDraw(true);
    }
    
    if (button_2.status === PsychoJS.Status.STARTED) {
      // check whether button_2 has been pressed
      if (button_2.isClicked) {
        if (!button_2.wasClicked) {
          // store time of first click
          button_2.timesOn.push(button_2.clock.getTime());
          button_2.numClicks += 1;
          // store time clicked until
          button_2.timesOff.push(button_2.clock.getTime());
        } else {
          // update time clicked until;
          button_2.timesOff[button_2.timesOff.length - 1] = button_2.clock.getTime();
        }
        if (!button_2.wasClicked) {
          // end routine when button_2 is clicked
          continueRoutine = false;
          
        }
        // if button_2 is still clicked next frame, it is not a new click
        button_2.wasClicked = true;
      } else {
        // if button_2 is clicked next frame, it is a new click
        button_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_2 hasn't started / has finished
      button_2.clock.reset();
      // if button_2 is clicked next frame, it is a new click
      button_2.wasClicked = false;
    }
    
    // *text_button_2* updates
    if (t >= 0.0 && text_button_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_button_2.tStart = t;  // (not accounting for frame time here)
      text_button_2.frameNStart = frameN;  // exact frame index
      
      text_button_2.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of testComponents)
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


function testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test' ---
    for (const thisComponent of testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox_f1.text',textbox_f1.text)
    psychoJS.experiment.addData('textbox_f2.text',textbox_f2.text)
    psychoJS.experiment.addData('textbox_f3.text',textbox_f3.text)
    psychoJS.experiment.addData('textbox_f4.text',textbox_f4.text)
    psychoJS.experiment.addData('button_2.numClicks', button_2.numClicks);
    psychoJS.experiment.addData('button_2.timesOn', button_2.timesOn);
    psychoJS.experiment.addData('button_2.timesOff', button_2.timesOff);
    // the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var delayComponents;
function delayRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'delay' ---
    t = 0;
    delayClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('delay.started', globalClock.getTime());
    // keep track of which components have finished
    delayComponents = [];
    delayComponents.push(text);
    
    for (const thisComponent of delayComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function delayRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'delay' ---
    // get current time
    t = delayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of delayComponents)
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


function delayRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'delay' ---
    for (const thisComponent of delayComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('delay.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_end_allKeys;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    key_resp_end.keys = undefined;
    key_resp_end.rt = undefined;
    _key_resp_end_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text_end);
    endComponents.push(key_resp_end);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_end* updates
    if (t >= 0.0 && text_end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_end.tStart = t;  // (not accounting for frame time here)
      text_end.frameNStart = frameN;  // exact frame index
      
      text_end.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_end.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_end.setAutoDraw(false);
    }
    
    // *key_resp_end* updates
    if (t >= 0.0 && key_resp_end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_end.tStart = t;  // (not accounting for frame time here)
      key_resp_end.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_end.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_end.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_end.clearEvents(); });
    }
    
    if (key_resp_end.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_end.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_end_allKeys = _key_resp_end_allKeys.concat(theseKeys);
      if (_key_resp_end_allKeys.length > 0) {
        key_resp_end.keys = _key_resp_end_allKeys[_key_resp_end_allKeys.length - 1].name;  // just the last key pressed
        key_resp_end.rt = _key_resp_end_allKeys[_key_resp_end_allKeys.length - 1].rt;
        key_resp_end.duration = _key_resp_end_allKeys[_key_resp_end_allKeys.length - 1].duration;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
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


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_end.corr, level);
    }
    psychoJS.experiment.addData('key_resp_end.keys', key_resp_end.keys);
    if (typeof key_resp_end.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_end.rt', key_resp_end.rt);
        psychoJS.experiment.addData('key_resp_end.duration', key_resp_end.duration);
        routineTimer.reset();
        }
    
    key_resp_end.stop();
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
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
