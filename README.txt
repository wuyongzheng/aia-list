Generate Google Map page from AIA's panel GP clinic list PDF file.

Step 1:
pdftotext -eol unix -nopgbrk -layout AIA-IHS-GP-ClinicListing.pdf
mv AIA-IHS-GP-ClinicListing.txt pass1.txt

Step 2:
Repeatedly run parse-pdf.py and fix errors
python parse-pdf.py < pass1.txt > pass2.txt

Step 3:
run `get-gps.sh` to get GPS coordinates from postal code

Step 4:
run `python gen-js.py pass3.txt postal-gps.txt > aia-data.js` to generate javascript.
