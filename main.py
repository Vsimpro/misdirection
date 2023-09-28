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
    return "Project 'mislead' on github: "

# Misdirection.
@app.route("/<file>")
def file(file):
    if file not in image_link_pair:
        return "404."

    user_agent = request.headers.get("User-Agent")
    if "discord" in user_agent or "Discord" in user_agent:
        # Serve the image for cdn.discord
        directory = "./pictures"
        filename = file
        
        return send_from_directory(directory, filename)

    # Serve the link for the user.
    return image_link_pair[file]


if __name__ == '__main__':
    app.run()