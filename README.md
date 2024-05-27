Implementing the Solution:

Let’s walk through the steps to implement and test the solution:

Create 'System_Diagnostic.py':

Open your terminal and create a new file named System_Diagnostic.py using your preferred text editor. Paste the code provided above into this file.

Set Executable Permissions:

Grant executable permissions to the script:

'sudo chmod +x System_Diagnostic.py'

Execute the script in the terminal:

'./System_Diagnostic.py'

=============================================================================

Testing the Solution:

To simulate high CPU usage, install the stress tool and run a stress test:

'sudo apt install stress'
'stress --cpu 8'

Run the Script Again:

Open another terminal window and navigate to the directory containing System_Diagnostic.py. Run the script again:

'./System_Diagnostic.py'

Automate with Cron:

Set up a cron job to run the System_Diagnostic.py script at regular intervals. 
Use crontab -e to edit your user's cron jobs and add an entry to run the script every 60 seconds:

'* * * * * /path/to/System_Diagnostic.py'
