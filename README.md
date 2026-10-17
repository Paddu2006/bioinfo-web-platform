# Bioinfo Web Platform

A Django-based web platform that brings bioinformatics tools
to the browser — no command line needed!
Built as Phase 4 - Project 1 of my bioinformatics-to-tech portfolio.

## Features

- DNA Sequence Analyzer
  - GC content calculation
  - Base composition with Chart.js visualization
  - Complement and reverse complement
  - Interpretation (AT-rich, GC-rich, Balanced)

- Mutation Detector
  - SNP detection between two sequences
  - Transition and transversion classification
  - Mutation rate and similarity calculation
  - Interactive pie chart

- FASTA Analyzer
  - Parse multiple sequences from FASTA format
  - Per-sequence GC content with color coding
  - Summary statistics

- Analysis History
  - All analyses stored in SQLite database
  - View past DNA, mutation and FASTA analyses

## Tech Stack

- Python 3.13
- Django 4.x
- SQLite
- Bootstrap 5
- Chart.js
- Font Awesome
- Git + GitHub

## Usage

Install Django:
pip install django

Run migrations:
python manage.py makemigrations
python manage.py migrate

Start server:
python manage.py runserver

Open browser:
http://127.0.0.1:8000

## Screenshots

DNA Analyzer — Enter any DNA sequence and get instant analysis
Mutation Detector — Compare two sequences and detect mutations
FASTA Analyzer — Paste FASTA content and analyze all sequences
History — View all past analyses stored in database

## Project Roadmap

- Phase 4 Project 1 - Bioinfo Web Platform - Done
- Phase 4 Project 2 - Health Tracking Mobile App - Coming soon
- Phase 4 Project 3 - WGS Automation Pipeline - Coming soon
- Phase 4 Project 4 - Cloud Deployment - Coming soon

## Author

Padma Shree Jena
Bioinformatics + Tech Enthusiast | Python | R | Bash | Django
GitHub: https://github.com/Paddu2006

## License

MIT License
