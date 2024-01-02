import streamlit as st
st.title("Travel Budget Tracker")

expenses = []

currency_symbols = {
    'AED': 'د.إ', 'AFN': '؋', 'ALL': 'L', 'AMD': '֏', 'ANG': 'ƒ', 'AOA': 'Kz',
    'ARS': '$', 'AUD': 'A$', 'AWG': 'ƒ', 'AZN': '₼', 'BAM': 'KM', 'BBD': 'Bds$',
    'BDT': '৳', 'BGN': 'лв', 'BHD': 'ب.د', 'BIF': 'FBu', 'BMD': 'BD$', 'BND': 'B$',
    'BOB': 'Bs.', 'BRL': 'R$', 'BSD': 'B$', 'BTC': '₿', 'BTN': 'Nu.', 'BWP': 'P',
    'BYR': 'Br', 'BZD': 'BZ$', 'CAD': 'C$', 'CDF': 'FC', 'CHF': 'CHF', 'CLF': 'UF',
    'CLP': '$', 'CNY': '¥', 'COP': '$', 'CRC': '₡', 'CUC': '$', 'CUP': '₱', 'CVE': '$',
    'CZK': 'Kč', 'DJF': 'Fdj', 'DKK': 'kr', 'DOP': 'RD$', 'DZD': 'د.ج', 'EGP': 'E£',
    'ERN': 'Nfk', 'ETB': 'Br', 'EUR': '€', 'FJD': 'FJ$', 'FKP': '£', 'GBP': '£',
    'GEL': '₾', 'GGP': '£', 'GHS': 'GH₵', 'GIP': '£', 'GMD': 'D', 'GNF': 'FG',
    'GTQ': 'Q', 'GYD': 'G$', 'HKD': 'HK$', 'HNL': 'L', 'HRK': 'kn', 'HTG': 'G',
    'HUF': 'Ft', 'IDR': 'Rp', 'ILS': '₪', 'IMP': '£', 'INR': '₹', 'IQD': 'ع.د',
    'IRR': '﷼', 'ISK': 'kr', 'JEP': '£', 'JMD': 'J$', 'JOD': 'د.ا', 'JPY': '¥',
    'KES': 'KSh', 'KGS': 'лв', 'KHR': '៛', 'KMF': 'CF', 'KPW': '₩', 'KRW': '₩',
    'KWD': 'د.ك', 'KYD': 'CI$', 'KZT': '₸', 'LAK': '₭', 'LBP': 'ل.ل', 'LKR': 'රු',
    'LRD': 'L$', 'LSL': 'M', 'LTL': 'Lt', 'LVL': 'Ls', 'LYD': 'ل.د', 'MAD': 'MAD',
    'MDL': 'lei', 'MGA': 'Ar', 'MKD': 'ден', 'MMK': 'K', 'MNT': '₮', 'MOP': 'MOP$',
    'MRO': 'UM', 'MUR': '₨', 'MVR': 'Rf', 'MWK': 'MK', 'MXN': '$', 'MYR': 'RM',
    'MZN': 'MT', 'NAD': 'N$', 'NGN': '₦', 'NIO': 'C$', 'NOK': 'kr', 'NPR': '₨',
    'NZD': 'NZ$', 'OMR': 'ر.ع.', 'PAB': 'B/.', 'PEN': 'S/', 'PGK': 'K', 'PHP': '₱',
    'PKR': '₨', 'PLN': 'zł', 'PYG': '₲', 'QAR': 'ر.ق', 'RON': 'lei', 'RSD': 'дин',
    'RUB': '₽', 'RWF': 'RF', 'SAR': 'ر.س', 'SBD': 'SI$', 'SCR': '₨', 'SDG': 'ج.س.',
    'SEK': 'kr', 'SGD': 'S$', 'SHP': '£', 'SLL': 'Le', 'SOS': 'Sh', 'SRD': '$',
    'STD': 'Db', 'SVC': '₡', 'SYP': '£', 'SZL': 'E', 'THB': '฿', 'TJS': 'ЅМ',
    'TMT': 'T', 'TND': 'د.ت', 'TOP': 'T$', 'TRY': '₺', 'TTD': 'TT$', 'TWD': 'NT$',
    'TZS': 'TSh', 'UAH': '₴', 'UGX': 'USh', 'USD': '$', 'UYU': '$U', 'UZS': 'UZS',
    'VEF': 'Bs', 'VND': '₫', 'VUV': 'VT', 'WST': 'WS$', 'XAF': 'FCFA', 'XAG': 'XAG',
    'XAU': 'XAU', 'XCD': 'EC$', 'XDR': 'SDR', 'XOF': 'CFA', 'XPF': 'CFPF', 'YER': '﷼',
    'ZAR': 'R', 'ZMK': 'ZK', 'ZMW': 'ZMW', 'ZWL': 'Z$'
}

def calculate_total_expenses():
    total = sum(expenses)
    return total

add_expense = st.number_input("Enter expense amount:", value=0)
expense_purpose = st.text_input("Enter expense purpose:")
currency = st.selectbox("Select currency:", options=list(currency_symbols.keys()))

if st.button("Add Expense"):
    expenses.append(add_expense)
    st.write(f"Added: {currency_symbols[currency]} {add_expense} for {expense_purpose}")

st.write("### Current Expenses:")
for index, expense in enumerate(expenses, start=1):
    st.write(f"Expense {index}: {currency_symbols[currency]} {expense} - {expense_purpose}")

total_expenses = calculate_total_expenses()
st.write(f"### Total Expenses: {currency_symbols[currency]} {total_expenses}")
