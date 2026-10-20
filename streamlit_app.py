import random

import streamlit as st


PRODUCTS = (
    {
        "id": "pencil",
        "name": "Pencil",
        "illustration": """
            <g transform="rotate(-38 200 130)">
                <rect x="174" y="48" width="52" height="148" rx="10" fill="#f4c542" stroke="#b78518" stroke-width="5"/>
                <path d="M174 182h52v31l-26 35-26-35z" fill="#efc59e" stroke="#b78518" stroke-width="5" stroke-linejoin="round"/>
                <path d="M192 227l8 21 8-21z" fill="#39433f"/>
                <path d="M174 68h52" stroke="#fff0a6" stroke-width="8"/>
                <rect x="174" y="48" width="52" height="28" rx="9" fill="#f28d8d" stroke="#b78518" stroke-width="5"/>
            </g>
        """,
    },
    {
        "id": "eraser",
        "name": "Eraser",
        "illustration": """
            <g transform="rotate(-12 200 130)">
                <rect x="110" y="82" width="180" height="105" rx="28" fill="#f7a8b8" stroke="#bd7184" stroke-width="6"/>
                <path d="M205 84v101" stroke="#fff0f2" stroke-width="8"/>
                <path d="M132 110h52" stroke="#ffdbe2" stroke-width="8" stroke-linecap="round"/>
            </g>
        """,
    },
    {
        "id": "apple",
        "name": "Apple",
        "illustration": """
            <path d="M200 99c-13-17-42-23-63-9-42 28-31 99 7 136 20 19 40 7 56 7s36 12 56-7c38-37 49-108 7-136-21-14-50-8-63 9z" fill="#ed6a5e" stroke="#b84b46" stroke-width="6"/>
            <path d="M200 95c-4-22 4-37 19-49" fill="none" stroke="#76533c" stroke-width="10" stroke-linecap="round"/>
            <path d="M207 67c20-24 48-17 51 4-17 14-38 14-51-4z" fill="#78b878" stroke="#4a8759" stroke-width="5"/>
            <path d="M158 130c-7 15-9 31-5 44" fill="none" stroke="#ffb2a4" stroke-width="9" stroke-linecap="round"/>
        """,
    },
    {
        "id": "banana",
        "name": "Banana",
        "illustration": """
            <path d="M117 91c23 83 80 126 157 111 22-4 39-17 47-35-24 13-54 13-83 1-40-17-69-51-87-100-8-21-21-30-36-27-13 3-20 22 2 50z" fill="#f5cf45" stroke="#c29a20" stroke-width="7" stroke-linejoin="round"/>
            <path d="M117 91l-15-19M319 167l16 8" stroke="#76533c" stroke-width="12" stroke-linecap="round"/>
            <path d="M149 109c18 45 46 75 81 91" fill="none" stroke="#ffe98a" stroke-width="9" stroke-linecap="round"/>
        """,
    },
    {
        "id": "milk",
        "name": "Milk",
        "illustration": """
            <path d="M151 91l25-38h48l25 38v148H151z" fill="#fff" stroke="#90aaa3" stroke-width="6" stroke-linejoin="round"/>
            <path d="M176 53h48l-9 38h-64z" fill="#d9eeea" stroke="#90aaa3" stroke-width="6" stroke-linejoin="round"/>
            <path d="M151 118h98v63h-98z" fill="#a8d9ce"/>
            <path d="M177 146c8-13 21-13 29 0-8 13-21 13-29 0z" fill="#fff"/>
            <path d="M193 139v14" stroke="#75b7a6" stroke-width="4" stroke-linecap="round"/>
        """,
    },
    {
        "id": "juice",
        "name": "Juice",
        "illustration": """
            <path d="M144 90h112l-12 149h-88z" fill="#fffaf0" stroke="#b79b6a" stroke-width="6" stroke-linejoin="round"/>
            <path d="M151 142h98l-8 91h-82z" fill="#f4a340"/>
            <path d="M198 142v-79h21" fill="none" stroke="#e77f56" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M168 109h62" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".8"/>
            <path d="M185 164c10-12 22-12 32 0" fill="none" stroke="#ffd078" stroke-width="7" stroke-linecap="round"/>
        """,
    },
)
PRICES = (100, 200, 300, 400, 500, 600, 700, 800, 900)
PRICE_WEIGHTS = (20, 20, 18, 15, 12, 6, 4, 2, 1)

st.set_page_config(page_title="Seller | English Market", page_icon="🛍️", layout="wide")

st.markdown(
    """
    <style>
    .block-container {
        max-width: 1100px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }
    .seller-header {
        padding: 2rem 2.25rem;
        margin-bottom: 1.5rem;
        border-radius: 24px;
        color: #fff;
        background: linear-gradient(120deg, #173b35, #287760);
    }
    .seller-eyebrow {
        margin: 0;
        color: #c5f3d5;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.16em;
    }
    .seller-header h1 {
        margin: 0.25rem 0 0;
        color: #fff;
        font-size: clamp(3rem, 8vw, 5rem);
        font-weight: 900;
        letter-spacing: 0.06em;
        line-height: 1;
    }
    .seller-header p {
        margin: 0.8rem 0 0;
        color: #e2f4eb;
        font-size: 1rem;
    }
    .product-title {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 0.5rem;
        margin: 0.45rem 0 0.15rem;
        color: #18352d;
        font-size: 1.25rem;
        font-weight: 750;
    }
    .product-title span {
        color: #75857f;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .product-illustration {
        display: block;
        width: 100%;
        aspect-ratio: 400 / 260;
        overflow: hidden;
        border-radius: 14px;
        background: #f3f8f4;
    }
    .price-result {
        padding: 0.65rem 0.75rem;
        margin-top: 0.5rem;
        border-radius: 12px;
        background: #eaf7ef;
        color: #176344;
        font-size: 1.45rem;
        font-weight: 800;
        text-align: center;
    }
    div.stButton > button {
        min-height: 2.8rem;
        border: 0;
        border-radius: 12px;
        background: #287760;
        color: #fff;
        font-weight: 700;
    }
    div.stButton > button:hover {
        background: #1c5b48;
        color: #fff;
    }
    div.stButton > button:disabled {
        border: 1px solid #dce5df;
        background: #f1f4f2;
        color: #829088;
    }
    @media (max-width: 640px) {
        .block-container { padding: 1.25rem 1rem 2rem; }
        .seller-header { padding: 1.5rem; border-radius: 18px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <header class="seller-header">
        <p class="seller-eyebrow">ENGLISH CLASS · MARKET</p>
        <h1>SELLER</h1>
        <p>Choose a product and find its price!</p>
    </header>
    """,
    unsafe_allow_html=True,
)
if "product_prices" not in st.session_state:
    st.session_state.product_prices = {}
if "special_product" not in st.session_state:
    st.session_state.special_product = random.choice(PRODUCTS)["id"]

for row_start in range(0, len(PRODUCTS), 3):
    columns = st.columns(3, gap="medium")
    for column, product in zip(columns, PRODUCTS[row_start : row_start + 3]):
        with column:
            with st.container(border=True):
                st.markdown(
                    f'<svg class="product-illustration" viewBox="0 0 400 260" '
                    f'role="img" aria-label="{product["name"]} illustration" '
                    f'xmlns="http://www.w3.org/2000/svg">'
                    f'<rect width="400" height="260" rx="18" fill="#f3f8f4"/>'
                    f'{product["illustration"]}</svg>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<div class="product-title">{product["name"]}</div>',
                    unsafe_allow_html=True,
                )
                if product["id"] in st.session_state.product_prices:
                    price = st.session_state.product_prices[product["id"]]
                    st.markdown(
                        f'<div class="price-result">{price:,}₩</div>',
                        unsafe_allow_html=True,
                    )
                    st.button(
                        "Price",
                        key=f"price_{product['id']}",
                        width="stretch",
                        disabled=True,
                    )
                elif st.button(
                    "Price",
                    key=f"price_{product['id']}",
                    width="stretch",
                ):
                    if product["id"] == st.session_state.special_product:
                        price = 1000
                    else:
                        price = random.choices(
                            PRICES,
                            weights=PRICE_WEIGHTS,
                            k=1,
                        )[0]
                    st.session_state.product_prices[product["id"]] = price
                    st.rerun()
