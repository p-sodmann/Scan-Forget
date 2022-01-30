[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/p-sodmann/Scan-Forget">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Scan&Forget</h3>

  <p align="center">
    Make your mail searchable with scanning and running tesseract.
    <br />
    <a href="https://github.com/p-sodmann/Scan-Forget"><strong>Explore the docs #TODO»</strong></a>
    <br />
    <br />
    <a href="https://github.com/p-sodmann/Scan-Forget/issues">Report Bug</a>
    ·
    <a href="https://github.com/p-sodmann/Scan-Forget/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
I needed a script to scan and search my documents. Unfortunately, my multifunction printer is too old to save directly to the NAS with it.
Because it still prints very well and the scan quality is perfectly adequate, I didn't want to dispose of it.
This script is an example of how to easily scan letters via [WIA (Windows Image Acquisition)](https://docs.microsoft.com/de-de/windows/win32/wia/-wia-startpage), save them as png and make them searchable with tesseract. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [python](https://www.python.org/)
* [tesseract](https://tesseract-ocr.github.io/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Run "main.py username" to get started. Then enter a title for the document to be scanned. When finished, you can either press [ENTER] directly to scan the next page of the same document, or enter a new title for the next document. "q" ends the script.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip install tesseract

### Installation

1. Clone the repository in a folder of your choice.
2. Run python main.py username

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Add simple example to search through the saved documents with simple keyword matching

See the [open issues](https://github.com/p-sodmann/Scan-Forget/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Philipp Sodmann - [@@psodmann](https://twitter.com/@psodmann)

Project Link: [https://github.com/p-sodmann/Scan-Forget](https://github.com/p-sodmann/Scan-Forget)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/p-sodmann/Scan-Forget.svg?style=for-the-badge
[contributors-url]: https://github.com/p-sodmann/Scan-Forget/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/p-sodmann/Scan-Forget.svg?style=for-the-badge
[forks-url]: https://github.com/p-sodmann/Scan-Forget/network/members
[stars-shield]: https://img.shields.io/github/stars/p-sodmann/Scan-Forget.svg?style=for-the-badge
[stars-url]: https://github.com/p-sodmann/Scan-Forget/stargazers
[issues-shield]: https://img.shields.io/github/issues/p-sodmann/Scan-Forget.svg?style=for-the-badge
[issues-url]: https://github.com/p-sodmann/Scan-Forget/issues
[license-shield]: https://img.shields.io/github/license/p-sodmann/Scan-Forget.svg?style=for-the-badge
[license-url]: https://github.com/p-sodmann/Scan-Forget/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/philipp-sodmann
[product-screenshot]: images/screenshot.png