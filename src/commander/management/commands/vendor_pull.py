from django.core.management.base import BaseCommand # this is the basic import that we need to do in all Custom comamnd files
from typing import Any  
from django.conf import settings  # This import is for usnig setting Configuration in this file 
import helper # this is Our own built package , that we are using to invoke functions that is written in helper package

STATICFILES_VENDOR_DIR = getattr(settings,"STATICFILES_VENDOR_DIR")

VENDOR_STATICFILES = {
    'flowbite.min.css':"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js" : "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
}

class Command(BaseCommand):
    help = 'Download vendor static files'
    def handle(self,*args : Any, **options : Any):
        # this is used to print things on the Terminal
        self.stdout.write("Downlaoding Vendor Files")
        # iterating through the Dictionary 
        completed_url = [] # list to store completed urls
        for filename, url in VENDOR_STATICFILES.items():
            self.stdout.write(f"Downloading {filename}..........")
            # calling the download function from helper package
            out_path = STATICFILES_VENDOR_DIR/filename
            dl_succes = helper.download_to_local(url,out_path)
            # Now Checks, Succesfully downloaded or not 
            if dl_succes :
                self.stdout.write(f"Downloaded {filename} successfully")
                completed_url.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {filename}")
                )

        # Now Checking taht all the urls in the Dictionary get downloaded or not 
        if set(completed_url) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS(" Succesfully updated vendor static files")
            )        
        else:
            self.stdout.write(
                self.style.WARNING("some files were not updated")
            )


