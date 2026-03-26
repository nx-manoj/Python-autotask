<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Study Log Bot</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap');

  :root {
    --bg: #0d0d0f;
    --surface: #141418;
    --surface2: #1c1c22;
    --border: #2a2a35;
    --accent: #7c6af7;
    --accent2: #4ecdc4;
    --text: #e8e8f0;
    --muted: #6b6b80;
    --success: #4ade80;
    --warn: #fbbf24;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px;
  }

  .container {
    width: 100%;
    max-width: 760px;
  }

  .header {
    display: flex;
    align-items: flex-end;
    gap: 16px;
    margin-bottom: 32px;
  }

  .badge {
    background: var(--accent);
    color: #fff;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 6px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  h1 {
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1;
  }

  h1 span { color: var(--accent); }

  .subtitle {
    color: var(--muted);
    font-size: 13px;
    font-family: 'JetBrains Mono', monospace;
    margin-top: 4px;
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 16px;
  }

  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
  }

  .card-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
  }

  .card-title {
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 6px;
  }

  .card-desc {
    font-size: 12px;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    line-height: 1.6;
  }

  .step-dot {
    display: inline-block;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: var(--accent);
    color: #fff;
    font-size: 10px;
    font-weight: 700;
    text-align: center;
    line-height: 20px;
    margin-right: 8px;
    flex-shrink: 0;
  }

  .step-dot.done { background: var(--success); color: #000; }
  .step-dot.active { background: var(--accent2); color: #000; }

  .steps-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
  }

  .steps-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 16px;
    font-family: 'JetBrains Mono', monospace;
  }

  .step-row {
    display: flex;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid var(--border);
    gap: 4px;
  }

  .step-row:last-child { border-bottom: none; }

  .step-text { font-size: 13px; }
  .step-code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--accent2);
    background: var(--surface2);
    padding: 2px 6px;
    border-radius: 4px;
    margin-left: auto;
  }

  .terminal {
    background: #0a0a0c;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    line-height: 1.8;
  }

  .term-bar {
    display: flex;
    gap: 6px;
    margin-bottom: 14px;
  }

  .dot { width: 10px; height: 10px; border-radius: 50%; }
  .dot.r { background: #ff5f57; }
  .dot.y { background: #febc2e; }
  .dot.g { background: #28c840; }

  .term-line { color: #6b6b80; }
  .term-line .prompt { color: var(--accent2); }
  .term-line .cmd { color: var(--text); }
  .term-line .out { color: #4ade80; }
  .term-line .comment { color: #3d3d4d; }

  .run-btn {
    width: 100%;
    padding: 16px;
    background: var(--accent);
    color: #fff;
    border: none;
    border-radius: 12px;
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 0.5px;
    transition: opacity 0.2s, transform 0.1s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin-bottom: 12px;
  }

  .run-btn:hover { opacity: 0.88; transform: translateY(-1px); }
  .run-btn:active { transform: translateY(0); }

  .run-btn.running {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--accent2);
    cursor: not-allowed;
  }

  .progress-bar {
    height: 3px;
    background: var(--border);
    border-radius: 2px;
    overflow: hidden;
    margin-bottom: 16px;
  }

  .progress-fill {
    height: 100%;
    background: var(--accent);
    border-radius: 2px;
    width: 0%;
    transition: width 0.4s ease;
  }

  .log-area {
    background: #0a0a0c;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    line-height: 1.9;
    min-height: 80px;
    max-height: 160px;
    overflow-y: auto;
  }

  .log-line { display: block; }
  .log-line.info  { color: var(--muted); }
  .log-line.ok    { color: var(--success); }
  .log-line.run   { color: var(--accent2); }
  .log-line.warn  { color: var(--warn); }

  .tip {
    background: var(--surface2);
    border-left: 3px solid var(--accent);
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    font-size: 12px;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    line-height: 1.7;
  }

  .tip strong { color: var(--accent2); font-weight: 700; }

  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
  .cursor { animation: blink 1s step-end infinite; }

  @keyframes spin { to { transform: rotate(360deg); } }
  .spinner {
    width: 14px; height: 14px;
    border: 2px solid rgba(255,255,255,0.3);
    border-top-color: #fff;
    border-radius: 50%;
    animation: spin 0.7s linear infinite;
    display: none;
  }
  .running .spinner { display: block; }
</style>
</head>
<body>
<div class="container">

  <div class="header">
    <div>
      <div class="badge">pyautogui + pygetwindow</div>
      <h1>Study Log <span>Bot</span></h1>
      <div class="subtitle">// real-life GUI automation example</div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <div class="card-label">What it does</div>
      <div class="card-title">Opens Notepad automatically</div>
      <div class="card-desc">Launches notepad.exe, waits for it to load, then focuses the window.</div>
    </div>
    <div class="card">
      <div class="card-label">Then</div>
      <div class="card-title">Types your daily log</div>
      <div class="card-desc">Auto-fills date, tasks, notes using pyautogui.typewrite() — no human needed.</div>
    </div>
    <div class="card">
      <div class="card-label">Finally</div>
      <div class="card-title">Saves the file</div>
      <div class="card-desc">Hits Ctrl+S, types the filename in the save dialog, and presses Enter.</div>
    </div>
    <div class="card">
      <div class="card-label">Schedule it</div>
      <div class="card-title">Runs every morning</div>
      <div class="card-desc">Add to Windows Task Scheduler — runs at 8AM daily with zero effort.</div>
    </div>
  </div>

  <div class="steps-card">
    <div class="steps-title">// how the script works — step by step</div>
    <div class="step-row">
      <span class="step-dot done">1</span>
      <span class="step-text">Script starts, waits 3 seconds (you switch to desktop)</span>
      <span class="step-code">time.sleep(3)</span>
    </div>
    <div class="step-row">
      <span class="step-dot done">2</span>
      <span class="step-text">Opens Notepad using subprocess</span>
      <span class="step-code">Popen(["notepad.exe"])</span>
    </div>
    <div class="step-row">
      <span class="step-dot active">3</span>
      <span class="step-text">Finds and activates the Notepad window</span>
      <span class="step-code">gw.getWindowsWithTitle()</span>
    </div>
    <div class="step-row">
      <span class="step-dot">4</span>
      <span class="step-text">Types study log content line by line</span>
      <span class="step-code">typewrite() + press('enter')</span>
    </div>
    <div class="step-row">
      <span class="step-dot">5</span>
      <span class="step-text">Saves file with keyboard shortcut</span>
      <span class="step-code">hotkey('ctrl', 's')</span>
    </div>
    <div class="step-row">
      <span class="step-dot">6</span>
      <span class="step-text">Types filename in Save dialog and confirms</span>
      <span class="step-code">typewrite(filename)</span>
    </div>
  </div>

  <div class="terminal">
    <div class="term-bar">
      <div class="dot r"></div>
      <div class="dot y"></div>
      <div class="dot g"></div>
    </div>
    <div class="term-line"><span class="comment"># Windows CMD / PowerShell</span></div>
    <div class="term-line"><span class="prompt">C:\Users\Manoj&gt; </span><span class="cmd">pip install pyautogui pygetwindow pyperclip</span></div>
    <div class="term-line"><span class="out">Successfully installed pyautogui pygetwindow pyperclip</span></div>
    <div class="term-line">&nbsp;</div>
    <div class="term-line"><span class="prompt">C:\Users\Manoj&gt; </span><span class="cmd">python study_log_bot.py</span></div>
    <div class="term-line"><span class="out">Starting in 3 seconds... switch to desktop!</span></div>
    <div class="term-line"><span class="out">Opening Notepad...</span></div>
    <div class="term-line"><span class="out">Typing study log...</span></div>
    <div class="term-line"><span class="out">Saving file...</span></div>
    <div class="term-line"><span class="out">Done! Saved as StudyLog_27-03-2026.txt</span></div>
    <div class="term-line"><span class="prompt">C:\Users\Manoj&gt; </span><span class="cursor">_</span></div>
  </div>

  <div class="progress-bar">
    <div class="progress-fill" id="progress"></div>
  </div>

  <button class="run-btn" id="runBtn" onclick="simulateRun()">
    <div class="spinner" id="spinner"></div>
    <span id="btnText">Simulate Bot Run</span>
  </button>

  <div class="log-area" id="logArea">
    <span class="log-line info">// press the button above to simulate the automation steps</span>
  </div>

  <br>
  <div class="tip">
    <strong>Pro tip —</strong> To run this every morning automatically, open <strong>Windows Task Scheduler</strong> &rarr; Create Basic Task &rarr; Daily at 8:00 AM &rarr; Action: Start a program &rarr; browse to <strong>python.exe</strong> &rarr; Arguments: <strong>study_log_bot.py</strong>. Your log will be ready before you even open your laptop.
  </div>

</div>

<script>
const steps = [
  { delay: 300,  cls: 'info', msg: '[00:00] Script started — waiting 3 seconds...' },
  { delay: 900,  cls: 'run',  msg: '[00:03] subprocess.Popen(["notepad.exe"]) called' },
  { delay: 1500, cls: 'ok',   msg: '[00:04] Notepad opened successfully' },
  { delay: 2000, cls: 'run',  msg: '[00:04] gw.getWindowsWithTitle("Notepad") — found!' },
  { delay: 2500, cls: 'run',  msg: '[00:05] win.activate() — window focused' },
  { delay: 3000, cls: 'run',  msg: '[00:05] pyautogui.click() — inside Notepad' },
  { delay: 3500, cls: 'run',  msg: '[00:05] Typing log content line by line...' },
  { delay: 5500, cls: 'ok',   msg: '[00:12] Log content typed (38 lines)' },
  { delay: 6000, cls: 'run',  msg: '[00:12] pyautogui.hotkey("ctrl", "s") — Save dialog' },
  { delay: 6600, cls: 'run',  msg: '[00:13] Typing filename: StudyLog_27-03-2026.txt' },
  { delay: 7200, cls: 'run',  msg: '[00:14] pyautogui.press("enter") — confirming save' },
  { delay: 7800, cls: 'ok',   msg: '[00:14] File saved: StudyLog_27-03-2026.txt' },
  { delay: 8200, cls: 'ok',   msg: '[00:14] Bot finished. No human interaction needed.' },
];

function simulateRun() {
  const btn = document.getElementById('runBtn');
  const logArea = document.getElementById('logArea');
  const progress = document.getElementById('progress');
  const btnText = document.getElementById('btnText');

  btn.classList.add('running');
  btnText.textContent = 'Bot running...';
  logArea.innerHTML = '';
  progress.style.width = '0%';

  const total = steps[steps.length - 1].delay;

  steps.forEach((s, i) => {
    setTimeout(() => {
      const span = document.createElement('span');
      span.className = 'log-line ' + s.cls;
      span.textContent = s.msg;
      logArea.appendChild(span);
      logArea.scrollTop = logArea.scrollHeight;
      const pct = Math.round(((i + 1) / steps.length) * 100);
      progress.style.width = pct + '%';

      if (i === steps.length - 1) {
        setTimeout(() => {
          btn.classList.remove('running');
          btnText.textContent = 'Run Again';
        }, 400);
      }
    }, s.delay);
  });
}
</script>
</body>
</html>
