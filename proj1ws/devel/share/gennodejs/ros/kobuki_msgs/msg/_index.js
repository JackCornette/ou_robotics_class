
"use strict";

let MotorPower = require('./MotorPower.js');
let DigitalInputEvent = require('./DigitalInputEvent.js');
let ButtonEvent = require('./ButtonEvent.js');
let DockInfraRed = require('./DockInfraRed.js');
let BumperEvent = require('./BumperEvent.js');
let Led = require('./Led.js');
let DigitalOutput = require('./DigitalOutput.js');
let CliffEvent = require('./CliffEvent.js');
let Sound = require('./Sound.js');
let PowerSystemEvent = require('./PowerSystemEvent.js');
let ScanAngle = require('./ScanAngle.js');
let RobotStateEvent = require('./RobotStateEvent.js');
let KeyboardInput = require('./KeyboardInput.js');
let SensorState = require('./SensorState.js');
let ControllerInfo = require('./ControllerInfo.js');
let VersionInfo = require('./VersionInfo.js');
let WheelDropEvent = require('./WheelDropEvent.js');
let ExternalPower = require('./ExternalPower.js');
let AutoDockingFeedback = require('./AutoDockingFeedback.js');
let AutoDockingAction = require('./AutoDockingAction.js');
let AutoDockingActionFeedback = require('./AutoDockingActionFeedback.js');
let AutoDockingActionResult = require('./AutoDockingActionResult.js');
let AutoDockingGoal = require('./AutoDockingGoal.js');
let AutoDockingResult = require('./AutoDockingResult.js');
let AutoDockingActionGoal = require('./AutoDockingActionGoal.js');

module.exports = {
  MotorPower: MotorPower,
  DigitalInputEvent: DigitalInputEvent,
  ButtonEvent: ButtonEvent,
  DockInfraRed: DockInfraRed,
  BumperEvent: BumperEvent,
  Led: Led,
  DigitalOutput: DigitalOutput,
  CliffEvent: CliffEvent,
  Sound: Sound,
  PowerSystemEvent: PowerSystemEvent,
  ScanAngle: ScanAngle,
  RobotStateEvent: RobotStateEvent,
  KeyboardInput: KeyboardInput,
  SensorState: SensorState,
  ControllerInfo: ControllerInfo,
  VersionInfo: VersionInfo,
  WheelDropEvent: WheelDropEvent,
  ExternalPower: ExternalPower,
  AutoDockingFeedback: AutoDockingFeedback,
  AutoDockingAction: AutoDockingAction,
  AutoDockingActionFeedback: AutoDockingActionFeedback,
  AutoDockingActionResult: AutoDockingActionResult,
  AutoDockingGoal: AutoDockingGoal,
  AutoDockingResult: AutoDockingResult,
  AutoDockingActionGoal: AutoDockingActionGoal,
};
