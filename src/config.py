"""Configuration settings for SERI"""

import os


class Config:
    """Configuration class for detection and clicking parameters"""
    
    # Detection settings
    CONFIDENCE_THRESHOLD = 0.8
    TARGET_IMAGE_PATH = os.path.join(os.path.dirname(__file__), '../assets/target.png')
    
    # Timing settings (in seconds)
    INTERVAL = 1.0  # Check for target every N seconds
    CLICK_DELAY = 0.5  # Delay after clicking
    
    def __init__(self):
        self.confidence = self.CONFIDENCE_THRESHOLD
        self.interval = self.INTERVAL
        self.click_delay = self.CLICK_DELAY
        self.target_image = self.TARGET_IMAGE_PATH
