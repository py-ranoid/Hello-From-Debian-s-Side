Note : Find project scrum board [here](https://storm.debian.net/grain/bD3aJdnYLBWo5R3K6GWckn/b/sandstorm/libreboard)

---
# Week 5

---
# Sorting out default country
If the number isn't in E.164 format, libphonenumber can't accomplish much with the number.
<br> Hence it's important to assign a default country code in such scenarios.

## Using environment variables
- Using `DEBDIALER_COUNTRY`

        export DEBDIALER_COUNTRY="IN"
