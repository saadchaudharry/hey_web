import os
import requests

# URL of the file you want to download
url_filename_mapping = {
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/images/logo.png": "logo.png",
    "https://mobirise.com/extensions/elevatem5/moving-service/assets/web/assets/mobirise-icons2/mobirise2.css": "mobirise2.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/bootstrap/css/bootstrap.min.css": "bootstrap.min.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/bootstrap/css/bootstrap-grid.min.css": "bootstrap-grid.min.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/bootstrap/css/bootstrap-reboot.min.css": "bootstrap-reboot.min.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/dropdown/css/style.css": "dropdown_style.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/socicon/css/styles.css": "socicon_style.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/theme/css/style.css": "theme_style.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/recaptcha.css": "recaptcha.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/mobirise/css/mbr-additional.css": "mbr-additional.css",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/bootstrap/js/bootstrap.bundle.min.js": "bootstrap.bundle.min.js",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/ytplayer/index.js": "index.js",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/dropdown/js/navbar-dropdown.js": "navbar-dropdown.js",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/embla/embla.min.js": "embla.min.js",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/embla/script.js": "embla_script.js",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/theme/js/script.js": "theme_script.js",
    # "https://mobirise.com/extensions/elevatem5/moving-service/assets/formoid.min.js": "formoid.min.js",
}

for url, filename in url_filename_mapping.items():  # Use items() to iterate through key-value pairs
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Specify the file path where you want to save the downloaded file
        file_path = os.path.join("assets", filename)

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Open the file in binary write mode and write the content
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded and saved as {file_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")











































# import requests
# import os
# import requests
# # URL of the file you want to download
# url_filename_mapping = {
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/images/logo.png":"logo.png" ,
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/web/https://mobirise.com/extensions/elevatem5/moving-service/assets/mobirise-icons2/mobirise2.css":"mobirise2.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/bootstrap/css/bootstrap.min.css":"bootstrap.min.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/bootstrap/css/bootstrap-grid.min.css":"bootstrap-grid.min.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/bootstrap/css/bootstrap-reboot.min.css":"bootstrap-reboot.min.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/dropdown/css/style.css":"dropdown_style.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/socicon/css/styles.css":"socicon_style.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/theme/css/style.css":"theme_style.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/recaptcha.css":"recaptcha.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/mobirise/css/mbr-additional.css":"mbr-additional.css",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/bootstrap/js/bootstrap.bundle.min.js":"bootstrap.bundle.min.js",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/ytplayer/index.js":"index.js",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/dropdown/js/navbar-dropdown.js":"navbar-dropdown.js",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/embla/embla.min.js":"embla.min.js",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/embla/script.js":"embla_script.js",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/theme/js/script.js":"theme_script",
#     "https://mobirise.com/extensions/elevatem5/moving-service/assets/formoid.min.js":"formoid.min.js",
# }



# for url, filename in enumerate(url_filename_mapping):
#     # Send an HTTP GET request to the URL
#     response = requests.get(filename)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Specify the file path where you want to save the downloaded file
#         file_path = os.path.join("downloaded_files", f"file{url}")

#         # Create the directory if it doesn't exist
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)

#         # Open the file in binary write mode and write the content
#         with open(file_path, 'wb') as file:
#             file.write(response.content)

#         print(f"File downloaded and saved as {file_path}")
#     else:
#         print(f"Failed to download file. Status code: {response.status_code}")