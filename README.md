# Keyword Suggestion MCP Server

## Overview

The **Keyword Suggestion MCP Server** is a powerful tool designed to assist with keyword research for both SEO (Search Engine Optimization) and PPC (Pay-Per-Click) campaigns. It provides keyword recommendations and search volumes, scored by relevance, to help optimize your content strategy and improve visibility across search engines.

## Features

- **Keyword Recommendation**: The server suggests keywords relevant to your input phrase, aiding in creating effective content or ad campaigns.
- **Search Volume Data**: Receive detailed search volume metrics for each suggested keyword, allowing for more informed decision-making in your marketing strategies.
- **Relevance Scoring**: All keyword suggestions are scored based on their relevance to your input, ensuring that you focus on the most pertinent options.

## Usage

### Tools and Functions

The server offers a straightforward interface with the following functions:

- **Keyword Suggestion (GET/POST)**: Recommends keywords for SEO and SEM scored by relevance.

### Parameters

- **phrase (required)**: The primary input keyword or phrase for which you seek suggestions.
- **lang (optional)**: Two-letter language codes to specify the language of interest. This helps in targeting keywords for specific linguistic audiences.
- **loc (optional)**: Two-letter location codes to target specific geographical areas.

### Limitations

- **Max Input Size**: Up to 14,336 Unicode characters, including whitespace and markup characters.
- **Rate Limitations**: The server allows up to 2 requests per 10 seconds for Keyword Suggestion queries. If you exceed this limit, you will encounter a "Too many requests" error message.
- **Server Capacity**: The server can initially handle 6 requests per second and scales up to accommodate more traffic. It is advisable to gradually increase your request rate to avoid failures.

### Security and Privacy

- The server prioritizes security and privacy by not storing any content on the server side, only logging transactions.
- For enhanced security, using the POST method is recommended over GET.
- The server maintains PCI compliance annually through third-party assessments.

The **Keyword Suggestion MCP Server** is an essential tool for marketers and content creators looking to enhance their keyword strategy with data-driven insights.