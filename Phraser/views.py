import os
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from subprocess import check_output, CalledProcessError, STDOUT
import difflib
import subprocess

def qs1(request):
    return render(request,"qs1.html")

def index(request):
    if request.method == "GET":
        context = {
            "code": "#use input box to give inputs \n#Always use x as input variable\nx=int(input(""))\n",
            "output": "",
            "python": "active",
            "user_input": ""
        }
        return render(request, "index.html", context=context)
    elif "run" in request.POST:
# The Run button was clicked, just run the Python code and display the output
        context = {
            "code": request.POST["code"],
            "output": "",
            "python": "active",
            "user_input": request.POST.get("user_input", "")
        }
        with open("main.py", "w") as f:
            f.write(request.POST["code"])

        user_input = request.POST.get("user_input", "")
        try:
            output = check_output(["python", "main.py"], input=user_input.encode(), stderr=STDOUT).decode()
        except CalledProcessError as e:
            output = e.output.decode()

        context["output"] = output
        return render(request, "index.html", context=context)
    elif "submit" in request.POST:
        with open("comparison/obtained.txt", "w"):
                pass
# The Submit button was clicked, run the Python code with different inputs, save the outputs to comparison/obtained.txt and display the last output
        context = {
            "code": request.POST["code"],
            "output": "",
            "python": "active",
            "user_input": request.POST.get("user_input", "")
        }
        with open("main.py", "w") as f:
            f.write(request.POST["code"])
        with open("comparison/obtained.txt", "a") as f:
            for i in [0, 10, 100, 3939, -39, 75]:
                # Use the number in the array as input
                user_input = str(i)
                try:
                    output = check_output(["python", "main.py"], input=user_input.encode(), stderr=STDOUT).decode()
                except CalledProcessError as e:
                    output = e.output.decode()

                # Write the input and output to the testcase file
                f.write("Input: {}\n".format(user_input))
                f.write("Output: {}\n".format(output))

# Read the last output from the testcase file and display it
        with open("comparison/obtained.txt", "r") as f:
            output = f.readlines()[-2]
        context["output"] = output

#comparinsion of two files and printing the result
        ex_file = "comparison/expected.txt"
        test_file = "comparison/obtained.txt"
        ex_fl_lns = open(ex_file).readlines()
        test_fl_lns = open(test_file).readlines()
        context = {}
        if ex_fl_lns == test_fl_lns:
            context['message'] = "Congrats 🤩🥳 your code meets all the requirements"
        else:
            difference = difflib.HtmlDiff().make_file(ex_fl_lns, test_fl_lns, ex_file, test_file)
            context['difference'] = difference
        return render(request, "testcase.html", context=context)
    else:
        return HttpResponseBadRequest("Invalid request inside index")

def findeff(request):
    if request.method == "POST" and "findeff" in request.POST:
        with open('main.py', 'r') as main_file:
            main_contents = [line.replace("print", "return", 1) if line.strip().startswith("print") else line for line in main_file if "input(" not in line]
        with open('comparison/Time_Complexity.py', 'w') as tc_file,open('comparison/Space Complexity.py', 'w') as sc_file:
            tc_file.write("import random\nimport big_o\ndef function(x):\n")
            for line in main_contents:
                tc_file.write('\t' + line)
            tc_file.write("\ndef positive_int_generator(n):\n\treturn random.randint(0, 10000)\nbest, others = big_o.big_o(function, positive_int_generator, n_repeats=50)\nprint(best)")
            # Space_Complexity.py
            sc_file.write("from memory_profiler import profile\n@profile\ndef my_func(x):\n")
            for line in main_contents:
                sc_file.write('\t' + line)
            sc_file.write("\nif __name__ == '__main__':\n\tmy_func(6)")

        # Run the Time_Complexity.py and Space_Complexity.py files
        time_result = subprocess.run(["python", "comparison/Time_Complexity.py"], capture_output=True, text=True)
        space_result = subprocess.run(["python", "comparison/Space Complexity.py"], capture_output=True, text=True)
        print(time_result)
        # Get the time and space complexity output
        time_output = time_result.stdout.strip()
       
        space_output = "\n".join(line for line in space_result.stdout.strip().split("\n") if "Filename:" not in line)
    
        return render(request, 'efficiency.html', context={'time_output': time_output, 'space_output': space_output})

    else:
        return HttpResponseBadRequest("Invalid request inside findeff")
