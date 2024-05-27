Python automation script to run a health check-up of the system based on the below requirements and send an alert via email notification.

Requirements:

Monitor CPU usage and send an alert if it exceeds 80%.
Monitor available disk space and send an alert if it drops below 20%.
Monitor available memory and send an alert if it’s less than 500MB.
Verify that the hostname “localhost” resolves to “127.0.0.1” and send an alert if it doesn’t.
If the system passes all the above requirement tests, then send an alert notifying "system is healthy.".

Implementing the Solution:

Let’s walk through the steps to implement and test the solution:

Create 'System_Diagnostic.py':

++ **Before proceeding to next steps, replace email provider and email Id and save the scrip**t ++

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
