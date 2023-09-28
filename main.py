from flask import Flask, request, send_from_directory


# Global Variables
app = Flask(__name__)

# store image names and their link counterpart here.
# images will have to be in the /pictures/ folder.
image_link_pair = {
    # image : link
    "example.gif" : "https://vsim.xyz"
}


# index.
@app.route('/')
def hello_world():
    return "Project 'mislead' on github: <a href='https://github.com/Vsimpro/misdirection'>Vsimpro/misdirection</a>"

# Misdirection.
@app.route("/<file>")
def file(file):
    if file not in image_link_pair:
        return "404."


    user_agent = request.headers.get("User-Agent")
    print(user_agent)
    if "discord" in user_agent or "Discord" in user_agent or "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.6; rv:92.0) Gecko/20100101 Firefox/92.0" == user_agent:
        # Serve the image for cdn.discord
        directory = "./pictures"
        filename = file

        return send_from_directory(directory, filename)

    # Serve the link for the user.
    print("Redirecting")
    return redirect(image_link_pair[f"{file}"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5500)
