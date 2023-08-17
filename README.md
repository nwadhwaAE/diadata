# Price Comparison Framework for MIMATIC Data

Introduction:
This GitHub repository contains a Python-based framework designed to address the task of capturing and comparing cryptocurrency market prices from various API endpoints. The framework periodically captures market prices from the DIA Oracle API, CoinGecko API, and DEXTools API, then compares the data against a third-party source. In case of significant divergence beyond an acceptable limit, the framework notifies a Discord channel. This README provides an overview of the framework's structure, approach, and solution.

Folder Structure:
The repository has the following folder structure:

    API folder contains API integration scripts:
        coingecko_api.py: API integration for CoinGecko market data.
        dextools_api.py: API integration for DEXTools market data.
        dia_api.py: API integration for DIA Oracle market data.

    UTILS folder includes utility scripts:
        comparison.py: Contains functions to compare market prices from different APIs.
        discord_integration.py: Integrates with Discord to send notifications.

    main.py: Main script that orchestrates data capture, comparison, and notification.

    requirements.txt: Lists required Python packages.

    .github/workflows/data_comparison.yml: GitHub Actions workflow for periodic execution.



The approach taken to tackle the problem involves the following steps:

    Data Capture: Market data is captured using the API integration scripts for DIA Oracle, CoinGecko, and DEXTools.

    Comparison: The captured market data is compared using functions defined in comparison.py. The comparison includes checking for divergence between the different API sources.

    Discord Integration: The framework integrates with Discord using discord_integration.py to send notifications when significant divergence is detected.

    GitHub Actions: The framework is set up to run periodically using GitHub Actions. The workflow is defined in data_comparison.yml.
