# Retirement Register

Items removed or de-referenced during the redesign. Nothing was removed until references, network requests and HTTP behaviour were checked first.

| Item | Action | Reason | Verification |
| --- | --- | --- | --- |
| `contact.php` | Deleted | Publicly served raw PHP source; PHP cannot run on GitHub Pages | No internal references remained after the contact form was replaced with `mailto:` + LinkedIn |
| `assets/js/form-contact.js` | Deleted | Dead code targeting a form that no longer exists; posted to `contact.php` | Script tag removed first; grep confirmed no remaining references |
| `/scripts/script1.js`, `/scripts/script2.js`, inline service-worker registration | Removed from `index.html` | Returned 404 and caused 4 console errors | Browser console is now empty |
| `assets/img/Designer.png` favicon reference | Replaced with `assets/img/favicon.svg` | Referenced file did not exist | All local asset references resolve |
| `assets/img/service/service-icon-bg.svg` | Created | Referenced CSS asset did not exist | CSS URL audit passes |
| `assets/img/banner.png` in `thank-you.html` | Replaced with `assets/img/ban.webp` | Referenced file did not exist | File exists |
| `owl.video.play.png` in `owl.carousel.min.css` | Replaced with `owl-video-play.svg` | Referenced file did not exist | File exists |
| `assets/pdf/resume.pdf` links | Repointed to `assets/pdf/CV.pdf` | Referenced file did not exist | All PDF references resolve |
| `ahttps://...` Netflix preview | Corrected to `https://...` | Malformed URL | Approved repair logged in `tools/verify_parity.py` |
| Legacy jQuery/plugin scripts (17 files) | De-referenced, retained on disk | Replaced by `assets/js/modern.js` | Only `modern.js` is loaded; legacy files kept pending explicit deletion sign-off |
| Unused SlickNav, Owl Carousel and Nivo Lightbox CSS | De-referenced, retained on disk | No matching markup or scripts remain | No console errors or failed requests |

## Deliberate content changes

- All displayed and interactive email addresses now use `kumar.knp.82@gmail.com`.
- Interactive phone link corrected to `tel:+917995035165`.
- Cognorise internship URL retained verbatim despite a known external HTTP 404.
