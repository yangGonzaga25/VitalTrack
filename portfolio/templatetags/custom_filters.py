from django import template

register = template.Library()

EXCHANGE_RATE = 56  # Example conversion rate (1 USD = 56 PHP)

@register.filter
def revenue_format(value, currency="PHP"):
    """Formats revenue only with currency symbols."""
    try:
        value = int(value)
        if currency == "USD":
            converted_value = value / EXCHANGE_RATE
            return f"${converted_value:,.2f}"
        return f"₱{value:,}"
    except ValueError:
        return value  # Return as is if conversion fails
