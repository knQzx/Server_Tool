<a href="#"><img src="https://camo.githubusercontent.com/38f5db5524ba43e7262dfbca1f7d3631ba127fb1596785dfd707d5fc671821c9/687474703a2f2f466f7254686542616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667" alt="PyPI" data-canonical-src="http://ForTheBadge.com/images/badges/made-with-python.svg" style="max-width: 100%;"></a></br>
<h1>A program for managing school computers</h1>
<h2>What is it??</h2>
<p>The program was conceived as a means to help teachers or administrators in schools and offices to manage PCs</p>
<h2>Explanations of the means of assistance</h2>
<img src="https://i.ibb.co/3yr0Lz4/image.png" alt="Пример">
<ul>
  <li>Open Terminal - a button that opens the UI interface of the terminal</li>
  <li>OFF - the button that turns off all the pcs that are in the file (more on that later)</li>
  <li>REBOOT - the button restarting all pcs</li>
  <li>CUSTOM COMMANDS - a drop-down list of commands that are pre-registered in the file. When a command is selected, it is automatically executed!!!</li>
  <li>IP drop-down list. They appear in the form of "pc - ip number". When you register the ip in the file, you can not neglect this !!!</li>
  <li>Then all the commands are similar, and again, the drop-down list immediately activates the command to the selected ip</li>
</ul>
<img src="https://i.ibb.co/X7tyZyk/image.png" alt="Пример">
<ul>
  <li>By pressing the run button, the command you have given is executed on all PCs</li>
</ul>
<h2>Let's talk about the files and what should be in them</h2>
<ul>
  <li>Commands file - commands (each with a new line)</li>
  <li>IP'S file is the PC's ip in the format "{computer number} - {ip}"</li>
  <li>password_for_admin file - in this file you should have only 1 line - the password from the admin</li>
</ul>
<p1>!!! sudo apt install sshpass !!!</p1>
