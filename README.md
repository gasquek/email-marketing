# GasqueK Marketing Email Service (GME)
> This repository contains email templates and the necessary code to send HTML emails via SMTP to multiple receivers. 

![GitHub Content](https://user-images.githubusercontent.com/42417723/194566766-91d19f39-8071-46f3-80a8-6721aa32e2dc.jpg)



## Tech Stack

- MJML
- (HTML + CSS)
- Python

## Developer guide

### Getting started
To develop emails you are required to have Python, Git, and MJML installed. If you do not have Python you can install it here: https://www.python.org and git from here: https://git-scm.com. MJML is available either as a VSCode plugin https://marketplace.visualstudio.com/items?itemName=attilabuti.vscode-mjml or available using `npm`; read more about MJML here: https://mjml.io/.

You can check the latest sources with the command:
```
git clone https://github.com/gasquek/email-marketing
```
### Building emails
Developing in HTML+CSS is not the same as writing HTML emails due to the very limited nature of email clients (this is an entire field in front-end engineering so check it out if you are interested). The emails that you send must be properly formatted for email clients. It is highly advised to use MJML for developing your email and compiling it using MJML to HTML. 

For information about the MJML language/syntax check out their website/documentation at: https://documentation.mjml.io/
### Compiling emails
Compiling emails can be done using two methods depending on your developer style. Either in VSCode directly or using MJML in the terminal. Depending on your usage, we advise that you look up the respective documentation for the plugin or the full software.

## Usage Guide

### Getting started
To send emails you are required to have Python and Git installed. If you do not have Python you can install it here: https://www.python.org and git from here: https://git-scm.com. 


You can check the latest sources with the command:
```
git clone https://github.com/gasquek/email-marketing
```

### Sending emails
__NOTE__: The script is currently configured to send emails using `info@gasquen.se`. 

You can only send HTML files and not MJML files. The emails that you send must be properly formatted for email clients. It is highly advised to use MJML for developing your email and compiling it using MJML to HTML. Writing HTML+CSS is not the same as writing HTML emails due to the very limited nature of email clients.


To send an HTML email, use the following command:
```
python code/send_html_email.py <recipient> <file> -t <subject>
```

An example:
```
python code/send_html_email.py info@gasquen.se mottagningen-22/final.html -t "Sushi är godare än pizza"
```

After running the above command you will be prompted for a password. The password is an Application Password (App Password). Read more about their usage here: https://support.google.com/accounts/answer/185833?hl=en

Application passwords are generally very insecure methods of authentication and this method will likely become deprecated in the future. The application-specific password for `info@gasquen.se` can be found in the committee's password manager. 

### External usage
For external usage (Not GasqueK) you must create an application-specific password for your email account if you are using Google Email Services. If your email provider is not Google you must modify the SMTP settings in the script `code/send_html_email.py`. How to change these settings is generally available on the web. Additionally, you must also change the sender's email in the script.
