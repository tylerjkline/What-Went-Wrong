# What Went Wrong?

This is a simple script and setup that allows you to enquire ChatGPT immediately from commandline to ask, what went wrong executing a command?

The command works as follows:

whatwentwrong "command"

This will execute "command", analyze its output with ChatGPT, and try to inform you what is likely wrong and how to fix it.


# Setup

Append the following bash script to your bashrc:

    echo 'function whatwentwrong() {
        # Get the first word of the command
        COMMAND_NAME=$(echo $1 | cut -d " " -f 1)
    
        # Execute the command and save its output
        OUTPUT=$(eval $@ 2>&1 | tee /dev/stderr)
        echo "$OUTPUT" > ~/${COMMAND_NAME}_output.txt
    
        # Analyze the output with the Python script
        python /path/to/analyze.py ~/${COMMAND_NAME}_output.txt
    }' >> ~/.bashrc

This function takes a command as an argument, executes it, saves its output to a text file named after the command, and then calls the Python script to analyze this output. Replace `/path/to/analyze.py` with the actual path to analyze.py

After adding the function to your `.bashrc` file, you need to reload the file with the `source` command to make the function available in your current shell:

    source ~/.bashrc

You also must go into your analyze.py file and provide your api key.
# Usage
Now you can use the `whatwentwrong` function in your shell. For example:

    whatwentwrong "ls -l"
Output:

    └─$ whatwentwrong "ls -l"
    total 24
    -rw-r--r--  1  630 Jun 23 04:37 analyze.py
    drwxr-xr-x 15 4096 Jun 23 03:14 Auto-GPT
    drwxr-xr-x 13 4096 Jun 23 02:59 gpt-engineer
    -rw-r--r--  1    1 Jun 23 04:34 _output.txt
    -rw-r--r--  1  248 Jun 23 04:22 Whatwentwrong.bash
    -rw-r--r--  1  646 Jun 23 04:17 What-went-wrong.py
    The potential error is that the permissions given for the files are not consistent. For example, the first file, analyze.py, has permissions of -rw-r--r--, but the last two files, Whatwentwrong.bash and What-went-wrong.py, have permissions of -rw-r--r--. This could potentially cause problems when trying to access the files by different users. To fix this, the permissions should be set consistently across all of the files. For example, all files could use permissions of -rw-rw-r--, or all files could use permissions of -rwxrwxrwx.
