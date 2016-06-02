======================================
SCRIPT FOR RefEmo (EPS04)
======================================
:Revised: 2012/05/24

Before the Experiment
----------------------

1. Check the daily signups on the REP website for the timeslots during your lab 
   shift.
   
2. Make sure that there are enough copies of the consent and debriefing forms 
   for your session.
   
3. Make sure the computer is ready.

   + If the computer is asleep, wake it up py pressing the spacebar. Unlock the 
     screen.
   + If the computer is off, turn it on. Once the OS has booted, log on to the
     \"exp\" account using the password.
   + Open a terminal by clicking on the terminal icon on the taskbar or by 
     going to Applications => Acccessories => Terminal
   + Change to the \"RefEmo\" directory by typing "cd RefEmo/" and hitting Enter.
   + Start the python script by typing "python run_RefEmo.py" and hitting Enter.
   + Verify that the screen asking for a subject number appears.

4. At the designated start time for the experiment, go to the LZ-2nd waiting area 
   and call for the students using the following procedure:

   + In a loud, clear voice, announce the experiment:

     *\"Hello! I am calling participants for Brian Siefke's EPS04
     experiment at (start time). When I say your name, please respond.\"* 
     Then list the names of all participants for that session, using first and 
     last names.
     
   + Make an honest and polite effort to pronounce difficult names.
   + Confirm the names of respondants by double-checking their names against your
     list.
   + Escort the participant(s) to the lab.

Once the Participants are in the Lab
------------------------------------

It is critically important that we document informed consent from
every participant in every experiment we run.  Follow these procedures
every time before running a participant in any experiment that
requires documentation of informed consent.

1. Verify that you are using the behavioral (NOT EEG) consent form. It should be 
   blue or a similar \"cool\" color.
   
#. Pick up two copies of the consent form for each participant. Print your name, 
   sign and write date and time in the \"Investigator/Research Staff\" section on 
   the last page of each form.
   
#. Give one copy to each participant and read the following statement:

   *\"Thank you for coming today.  We appreciate your participation in this
   experiment. Some of the stimuli w will show you may be considered
   sensitive or offensive.  You will be able to speak to us at any time during the
   experiment if you have any concerns of difficulties, and you may withdraw from
   the study at any time with no loss of benefits or incentives.*

   *Please read and review this consent form.  It contains important information
   about this experiment and your rights as a research participant.  If you have 
   any questions, please let me know.  If you agree to participate in this study, 
   please print your name, sign, and date here on the last page of the form.\"* 
   <Point out the signature portion of the form.>
   
#. Give the participant(s) time to read over the consent form. While they are 
   reviewing the consent form, enter the information on the subject checklist 
   for each participant: subject number, time, date, room letter, and your 
   initials under \"Exptr.\"
   
#. After the participants have finished reading the information sheet, ask:

   *\"Do you have any questions about participating in this study?\"* 
   <Answer any questions they may have.>
   
#. If someone does not agree to participate, thank them for their time and notate 
   the fact in the Participant Incident Log.  If they wrote on the consent form, 
   write VOID in large letters across the front of the form and file it in the
   \"Completed Consent Forms\" file.  The lab manager or one of the senior lab 
   personnel will destroy the form when they process the file at the end of the day.
   
#. After the participants have consented,

   + collect the signed forms,
   + double check to make sure that they have properly completed the \"Signing 
     the consent form\" section and that you have filled out the \"Investigator /
     Research Staff\" section,
   + file the signed copy in the \"Completed Consent Forms\" file, 
   + and give each participant a copy that you have signed to keep.

After obtaining informed consent, ask students to turn off all cell phones, 
mp3 players, and other electronic devices. 

Personality Survey
------------------

*Give each participant a copy of the BFAS-ON sheet, then read the following
instructions:*

\"The first task in the experiment is a brief personality survey. The survey lists
a number of different characteristics that may or may not describe you. For each
statement, please indicate the extent to which that characteristic describes you using
a scale from 1 to 5, where 1 indicates that you strongly disagree that the statement
describes you and 5 indicates that you strongly agree that it describes you. Please be
as honest as possible, but rely on your initial feeling and do not think too much about
each item.\"

*Give the participants a few minutes to complete the survey, then collect the surveys.*


Starting the Experiment
-----------------------

*If you have not already started the python script, follow the instructions above 
to start it.*

*Type in the participant ID from the subject checklist and click START. A screen 
will appear asking for the subject's gender, age, race, and ethnic origin. 
Read the following statement to the participant(s):*

\"We woul now like to collect some demographic information. This 
information is for statistical use only and will not be linked to your identity 
in any way. When you are done with the form, please click OK and wait for further 
instructions.\"

*When all the participants have completed the demographics form, verify the 
startup information in the terminal window. Double-check to make sure that 
subject number is correct, then hit the ENTER key to begin the pyEPL script*

*Read the following set of instructions. (Some of these will also appear on the 
computer screen.)*
 
INSTRUCTIONS
------------

As you can see, instructions for the experiment are displayed on the computer 
screen. I will be going through these instructions with you. If you have any 
questions at any time, please feel free to interrupt me and ask them.

.. Initial instructions

In the experiment, you will be performing a task called the "refreshing task" that measures how well you are able to keep information in your short-term memory.  There are three parts to the refreshing task.

The task will start with a fixation cross in the middle of the screen. Please focus your attention on the cross. After about a second, two pictures will be shown on the screen, one on each side of the fixation cross.  When you see these pictures, try to commit them to memory.

Do you have any questions so far? *[Answer them, if any]*

Please press ENTER to continue.

.. Refresh instructions

After 1 second, the two images will disappear and the fixation cross will then change into an arrow pointing either left or right. When you see the arrow, please think about the image you just saw that was presented on the pointed side. For example, if the arrow points to the left, think about the picture previously presented on the left. 

As you think about the image, you will be asked whether the main content of the image was human or non-human. If you remember a person in the picture, press "J" (with your right index finger). If you do not remember a person, press "K" (with your right middle finger) for non-human.  You will have just over a second to make your response, so please do so as quickly as you can without sacrificing accuracy.

Do you have any questions about this task? *[Answer them, if any]*

Please press ENTER to continue.

.. Refresh practice instructions

Before beginning the experiment we will go through a few practice trials to give you a better feel for the refreshing task.

Remember to try to commit both images to memory, then think back to the one on the side the arrow points to and indicate whether it contained a person or not.

Do you have any questions before we being the practice? *[Answer them, if any]*

OK. Please press ENTER to start the practice.

*[Wait for participants to finish the practice]*

.. Refresh start instructions

We are now about to start the actual experiment. 

The experiment will consist of a series of blocks of trials, each containing about 15 refresh trials. Again, in each trial you will see a pair of images. After each pair is presented, you will need to briefly think about the image on the side the arrow points to and make the judgment of human vs. non-human. 

After each block you will be given a short break; when you are ready to start the next block, hit any key.

Before beginning the experiment tasks, do you have any questions? *[Answer them, if any]*

OK, when you are ready to begin the experiment, press ENTER.

MEMORY TEST
-----------

**NOTE:** *Instructions for the last part of the experiment (a surprise memory test) are 
displayed on the screen after subjects finish the refreshing blocks. Normally, 
participants will read the instructions
and go straight to the test, so you will not have to do anything. However,
some participants may open the door and ask questions. Be prepared to explain the
memory test task to them. The instructions that are displayed on the screen are:*

You're almost done, but there is one more task we would like you to
do: We want to see how well you remember the images that you saw
during the refreshing task.

In the next part of the experiment, we will present old images from
the refreshing task along with new images that you did not see.  For 
each test image, please indicate whether you think it is an old image 
(i.e., one you saw earlier) or a new image (i.e., one you did not 
see in the refreshing task).  Please press "J" if you think
the image is an old item or "K" if you think it's a new item.

You will only have about a second to make your response, so please respond
as quickly and accurately as possible before the next image comes up.

If you have any questions, please ask the experimenter now.  Otherwise,
press ENTER to begin a short practice memory test.

<After the practice>

If you have any questions about the memory test task, please ask 
the experimenter now. Otherwise, press ENTER to begin the memory test.


After the Experiment
--------------------

+ Exit the python script by pressing ENTER twice to return to the terminal prompt.
+ Escort the participants out of the lab area.
+ Backup the data by typing \"python backup_data.py\" at the Terminal and hitting
  Enter.
