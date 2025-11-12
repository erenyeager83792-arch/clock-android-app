"""Simple Clock Android App using pyandroid-dev"""
import time
from datetime import datetime
try:
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
    
    # Import Android UI components
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    TextView = autoclass('android.widget.TextView')
    LinearLayout = autoclass('android.widget.LinearLayout')
    Gravity = autoclass('android.view.Gravity')
    Color = autoclass('android.graphics.Color')
    ANDROID = True
except ImportError:
    ANDROID = False
    print("Running in non-Android environment")

class ClockApp:
    def __init__(self):
        self.running = True
        self.time_label = None
        
    @run_on_ui_thread
    def setup_ui(self):
        """Setup the Android UI"""
        if not ANDROID:
            return
            
        # Get the current activity
        activity = PythonActivity.mActivity
        
        # Create a LinearLayout
        layout = LinearLayout(activity)
        layout.setOrientation(LinearLayout.VERTICAL)
        layout.setGravity(Gravity.CENTER)
        layout.setBackgroundColor(Color.parseColor("#1a1a1a"))
        
        # Create TextView for displaying time
        self.time_label = TextView(activity)
        self.time_label.setText("00:00:00")
        self.time_label.setTextSize(60)
        self.time_label.setTextColor(Color.parseColor("#00ff00"))
        self.time_label.setGravity(Gravity.CENTER)
        
        # Add TextView to layout
        layout.addView(self.time_label)
        
        # Set the layout as content view
        activity.setContentView(layout)
    
    @run_on_ui_thread
    def update_time(self, time_str):
        """Update the time display"""
        if self.time_label:
            self.time_label.setText(time_str)
    
    def run(self):
        """Main app loop"""
        if ANDROID:
            self.setup_ui()
        
        while self.running:
            current_time = datetime.now().strftime("%H:%M:%S")
            
            if ANDROID:
                self.update_time(current_time)
            else:
                print(f"Current Time: {current_time}")
            
            time.sleep(1)

if __name__ == "__main__":
    app = ClockApp()
    try:
        app.run()
    except KeyboardInterrupt:
        app.running = False
        print("Clock app stopped")
