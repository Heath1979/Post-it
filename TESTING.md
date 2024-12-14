# Testing

This is the TESTING file for the [Post It](add_deployed_url) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
   - [Known bugs](#known-bugs)

## Validation

### HTML Validation

We used [HTML W3C Validator](https://validator.w3.org) to validate all of the HTML files.

Due to using Jinja syntax such as '{% extends "base.html" %} we had to use a different approach to checking the HTML as the validator would show errors if copying the HTML direct from the files in the Post It project. The method used to check the HTML was as follows:

- Using the deployed version from Heroku I navigated to each page.
- Right clicking on the page brought up a options menu with the option to view the page source located at the bottom.
- The complete HTML code for that page will then appear in a separate window.
- Copy that code and paste into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, and then repeat the steps to revalidate.

![html validation](documentation/testing/validator_clear.png) 

All HTML pages were validated and the pages generated solely by myself received a 'No errors or warning to show' result as shown above.

| HTML source Code/Page | Errors | Warnings |
| ---- | ----- | ------|
| Blogs | 0 | 0 |
| Blog Post | 0 | 0 |
| Register | 4 | 0 |
| Log in | 0 | 0 |
| Log out | 0 | 0 |

<hr>

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the small amount of JavaScript code added to the project. External JS, for Bootstrap purposes, obtained via [CDN](https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css) was not validated through JSHint.

| Page | Screenshot | Errors | Warnings |
| ---- | ------ | ------ | ------ | 
| post_detail.html | ![js from post_detail.html](documentation/testing/) | none | none |

<hr>

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com) was used to validate the Python files that were created or edited by any member of the team. No issues presented. Screenshots have been icluded with the results below.

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
| ---- | ---- | ------- | ------ | ----- | -----|
| Config | n/a | n/a | n/a | [No Errors](documentation/testing/) | n/a |
| Event | [No Errors](documentation/testing/) | [No Errors](documentation/testing/) | [No Errors](documentation/testing/) | [No Errors](documentation/testing/) | [No Errors](documentation/testing/) |

<hr>

### CSS Validation

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file. External CSS for Bootstrap, provided by [CDN](https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css) was not tested. 

![css validation](documentation/testing/)
  
<hr> 

### Lighthouse Scores

Lighthouse testing was carried out in Incognito mode to acheive the best result. Performance was lower than preferred due to the site being image heavy. Static images used in the sites design were saved in webp. Image types added by a site admin are at there own discretion and could affect the score. The CDNs used for Bootstrap were also noted in the Lighthouse report as causing issue with performance. This report will be reviewed for future development of Post It to raise this score.
  
![Lighthouse scores paginated posts](documentation/testing/)
*Desktop Paginated Blogs Page*

![Lighthouse scores event post](documentation/testing/)
*Desktop Blog Post Page*  
  
<hr>

### Wave Accisibility Evaluation 

![WAVE Web Accessibility Evaluation Tools](documentation/testing/)

The WAVE report tool was used to check accesability

## Manual Testing

### User Input/Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process the input appropriately.

| Feature | Tested? | User Input required | User Feedback Provided | Pass/Fail | Fix |
| ------- | ------- | ------------------- | ---------------------- | --------- | --- |
| Navbar | Yes | Click | The user is directed to the specific page as intended | Pass | - |
| Register Page | Yes | Username/Password. Email is optional | Empty username and password fields prompt the user. [username/password](documentation/testing/) too similar, password too short | Pass | - |
| Login | Yes | Username and Password | Username and Password must be exactly as originally registered. User notified once successfully signed in. | Pass | - |
| Blog Post Links | Yes | Click | User is taken to intended location via a new tab | Pass | - |
| Comment Box (Registered User) | Yes | Text input accepted | User is thanked for their comment | Pass | - |
| Edit Comment (Registered, Author) | Yes | Click button to choose Edit | Comment appears in comment box for update and update button appears underneath. When pressed the user is infomred that the comment has been updated | Pass | - |
| Delete Comment (Registered, Author) | Yes | Click button to choose Delete comment | A [modal](documentation/testing/) pops up asking the user if they are sure they want to delete their comment | Pass | - |


### Browser Compatibility 

Happy Heath was tested on the following browsers. New users were created and old users data edited. All features were tested and no issues found:

- Chrome v131.0.6778.86
- Edge v131.0.2903.51
- Safari v18.1.1

<hr>

### Testing User Stories 

User Stories are documented in the Happy Heath [Github Projects Board](link_to_project_board). User Stories are numbered, with Acceptance Criteria and Tasks detailed within. All features were tested to ensure that they provided the user with the expected output and action.

| User Story | Acceptance Criteria Met? | Tested | Response | Pass/Fail | Fix |
| ---- | ---- | ----- | ---- | ----- | ---- |

<hr>

### Dev Tools/Real World Device Testing

Responsive testing was carrired out using Google Dev Tools on the devices detailed within the below table. Responsiveness was evident on all features throughout all tested devices. Occassionally I would have to refresh the page as the page would load zoomed in or out on the simualted device. When refreshed and CSS checked the desired outcome was observed. I put this down to a caching issue in Chrome as this issue was not observed when testing on the available real world devices.
  
**Dev Tools Device Testing**
| Device | Feature | Issue | Fix |
| ---- | ----- | ---- | ----- |

**Real World Device Testing**
| Device      | Feature    | Issue  | Fix  | 
| ------------| ---------- | ------ |------|
| MSI Modern 15 H B13M | All features | No issues | None needed |

## Bugs

| No. | Bug | Solved | Fix | Commit no. |
| --- | ---- | ----- | --- | ---------- |

### Known bugs
