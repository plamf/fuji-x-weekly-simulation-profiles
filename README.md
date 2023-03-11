# Fuji X Weekly Simulation Profiles

Here you'll find a collection of Film Simulation Recipes parsed from https://fujixweekly.com/

## Motivation
Having to input every recipe on my camera is no fun at all, so I rarely do it.
That's a shame though, because simulation recipes are the heart and soul of Fujifilm cameras.

When I learned that you can input them in Fuji X Raw Studio and save them on your camera, I was thrilled. This made trying out different recipes on my own RAW files much easier. But still... I wanted to try them all, and quickly switch between profiles.

So I did what any Programmer would do: Instead of spending 5 hours to manually do something, I spent 20 hours automating the process!

## Disclaimer
Parsing text is awful. Parsing text that has been input by a human is torture.
That's why I can't confirm that all the values of every recipe are 100% correct. If the author provided ranges for values (like `0 to +1/3`), I always take the first value. I did, however, test every single one of the recipes I'm releasing here with my own Camera and Fuji X Raw Studio.

I'm not going to release the actual parser here, because I don't want people to DDoS Fuji X Weekly with hundreds of requests. I'm just going to provide the templates, which you'll have to convert with a master-template of your own.

At the moment, I'm only going to provide Profiles for X-Trans IV sensors, as these are the only ones I can test on my camera. While I could theoretically parse every single recipe for the other sensors, I don't feel comfortable releasing something I did not test.

## Ok, how do I use these Profiles with Fuji X Raw Studio on Windows?
### Prerequisites
1. Python 3.10 (I recommend typing `python` in the command prompt and installing it from the Windows store, otherwise install from here https://www.python.org/downloads/)
2. Fuji X Raw Studio (https://fujifilm-x.com/en-gb/support/download/software/x-raw-studio/)

### Making the profiles work with your camera
1. You'll need to create a master profile with X Raw Studio to use as a template. This is needed because we have to copy your camera model, serial number and some other fixed values to the profiles in order to make them work. You have to do this for every different camera model you're using.
2. Find the profile you just created. On Windows, they are usually here `%USERPROFILE%\AppData\Local\com.fujifilm.denji\X_RAW_STUDIO`
3. Copy the path of your master profile
4. Download the profiles you need from the releases page (https://github.com/plamf/fuji-x-weekly-simulation-profiles/releases) or just clone the repo
5. Open a command shell in the folder with your profiles of choice and run `python fx-templater.py "path/to/your/master/profile.FP1"`
6. The converted profiles should appear in a subfolder called `converted`
7. Copy the profiles into the same path where you got your master template from
8. You can now delete the master template and start Fuji X Raw Studio. All the profiles should be there!
9. **BONUS TIP**: If you want to know more about a certain recipe, open the `FP1` file in a text editor. I've included a link to https://fujixweekly.com/ in every file.

## Additional resources
The website I'm getting all these recipes from (consider donating to them!): https://fujixweekly.com/

How to use simulation recipes in Fuji X Raw Studio and save them to your camera: https://www.youtube.com/watch?v=IrGVsvo0Dx0
