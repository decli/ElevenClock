from ctypes import c_int, windll
windll.shcore.SetProcessDpiAwareness(c_int(2))


import io
from types import FunctionType


from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

BLOCK_RELOAD: bool = False

def loadTimeFormat():
    print("🟡 loadTimeFormat function has not been defined yet!")

def updateIfPossible():
    print("🟡 updateIfPossible function has not been defined yet!")

def restartClocks():
    print("🟡 restartClocks function has not been defined yet!")

def closeClocks():
    print("🟡 closeClocks function has not been defined yet!")

def _(a):
    try:
        raise NotImplementedError("_ function has not been defined!")
    except Exception as e:
        print("🟠", e)
    return a


app: QApplication = None
buffer: io.StringIO = None
old_stdout: io.StringIO = None
mController: object = None
TrayIcon: QSystemTrayIcon = None
SettingsWindow: QMainWindow = None
ww: QMainWindow = None
TemporaryDirectory: str = None
dateTimeFormat: str = "%HH:%M\n%A\n%d/%m/%Y"
settingsCache = {}
canEraseTempDirs: bool = False
newInstanceLaunched: bool = False

windowRects: dict[int, tuple[int, int, int, int]] = {}
windowTexts: dict[int, str] = {}
windowVisible: dict[int, bool] = {}
windowList: list[int] = []
newWindowList: list[int] = []
foregroundHwnd: int = 0
doCacheHost: bool = False
notTextInputHost: list[int] = []
cachedInputHosts: list[int] = []
previousFullscreenHwnd: dict[int, int] = {}
blockFullscreenCheck: bool = False
clocks: list[QWidget] = []

CustomSettings: type = None # This will be used then from the tools module to load CustomSettings instances (see function tools.py>openClockSettings())

blacklistedFullscreenApps: tuple = ("", "Program Manager", "NVIDIA GeForce Overlay", "NVIDIA GeForce Overlay DT", "ElenenClock_IgnoreFullscreenEvent") # The "" codes for titleless windows


settingsList: list[str] = [
    "DisableAutoCheckForUpdates",
    "DisableAutoInstallUpdates",
    "EnableSilentUpdates",
    "BypassDomainAuthCheck",
    "DisableSystemTray",
    "HideTaskManagerButton",
    "EnableSecondClock",
    "DisableHideOnFullScreen",
    "NewFullScreenMethod",
    "TransparentClockWhenInFullscreen",
    "MouseEventTransparentFS",
    "DisableHideWithTaskbar",
    "HideClockWhenClicked",
    "EnableLowCpuMode",
    "DisableNotifications",
    "DisableToolTip",
    "ForceClockOnFirstMonitor",
    "HideClockOnSecondaryMonitors",
    "CustomClockClickAction",
    "CustomClockDoubleClickAction",
    "CustomClockMiddleClickAction",
    "ClockClickToggleSetting",
    "DoubleClickToggleSetting",
    "MiddleClickToggleSetting",
    "ShowDesktopButton",
    "ClockOnTheLeft",
    "ForceOnBottom",
    "ForceOnTop",
    "PinClockToTheDesktop",
    "ClockFixedHeight",
    "ClockFixedWidth",
    "ClockXOffset",
    "ClockYOffset",
    "UseCustomFont",
    "UseCustomFontSize",
    "CustomLineHeight",
    "DisableAutomaticTextColor",
    "UseCustomFontColor",
    "DisableTaskbarBackgroundColor",
    "UseCustomBgColor",
    "UseCustomBgColor",
    "AccentBackgroundcolor",
    "DisableBlurryTexture",
    "CenterAlignment",
    "CustomClockStringsDisabled"
    "CustomClockStrings",
    "DisableTime",
    "EnableSeconds",
    "DisableDate",
    "EnableWeekNumber",
    "EnableWeekDay",
    "EnableInternetTime",
    "AtomicClockURL",
    "AtomicClockSyncInterval",
    "TooltipUseCustomFont",
    "TooltipUseCustomFontSize",
    "TooltipUseCustomFontColor",
    "TooltipDisableTaskbarBackgroundColor",
    "TooltipUseCustomBgColor",
    "PreventSleepFailure",
    "DisableLangAutoUpdater",
    "LogFullScreenAppTitle",
    "EnableWin32API",
    "EnableHideOnRDP",
    "legacyFullScreenMethod",
    "DisableSystemClockCover",
    "PerformanceTextUpdateInterval",
    "PerformanceClockLoopInterval",
    "PerformanceScreenCheckInterval",
    "PerformanceWnfDataInterval",
    "PerformanceBackgroundCheckRate",
]