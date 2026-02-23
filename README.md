 # Amazon Web Scraper

 App that scrapes Amazon product data via Oxylabs Web Scraper API, stores products in a database, discovers competitors, and generates AI-based competitor analysis.

  ## Features

  - Scrape a product by ASIN
  - Store product snapshots in PostgreSQL
  - Discover and scrape competitor products
  - AI analysis of positioning and recommendations (OpenAI via LangChain)

  ## Tech Stack

  - Python 3.11+
  - Streamlit
  - PostgreSQL 16
  - `psycopg` (Postgres driver)
  - Oxylabs Web Scraper API
  - LangChain + OpenAI

  ## Environment Variables

  Copy .env.example to .env and set real credentials:

  ```cp .env.example .env```

  Required values:

  - OXYLABS_USERNAME
    - Change me
  - OXYLABS_PASSWORD
    - Change me
  - OPENAI_API_KEY
    - Change me
  - POSTGRES_HOST
  - POSTGRES_PORT
  - POSTGRES_DB
  - POSTGRES_USER
  - POSTGRES_PASSWORD

  ## Run with Docker

  ```docker compose up -d --build```

  App:

  - http://localhost:8501

  Stop:

  ```docker compose down```

  Reset database (removes all data):

  ```docker compose down -v --remove-orphans```

  ## Input Values

  - **ASIN**  
    - **Definition:** Amazon Standard Identification Number.  
    - **Where to find it:** In the Amazon product URL (`/dp/ASIN`).

  - **Geo**  
    - **Definition:** Delivery location / country context used for scraping.  
    - **Where to find it:** Defined by the user’s selected marketplace.

  - **Domain**  
    - **Definition:** Amazon marketplace domain.  
    - **Where to find it:** Directly in the Amazon URL domain (e.g., `amazon.com`, `amazon.de`).

  ## How It Works

  1. User enters ASIN + geo + domain in Streamlit UI.
  2. App fetches product details from Oxylabs and stores them in Postgres.
  3. App can discover competitors based on the parent product.
  4. Competitors are scraped with progress updates in UI.
  5. AI model analyzes parent + competitors and returns summary/recommendations.
