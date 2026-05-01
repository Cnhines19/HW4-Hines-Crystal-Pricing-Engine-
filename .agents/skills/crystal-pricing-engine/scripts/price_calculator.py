def calculate_price(stone, weight_grams, quality, cut):
    # Base price per gram (example baseline values)
    base_prices = {
        "labradorite": 0.15,
        "amethyst": 0.10,
        "rose quartz": 0.08,
        "black tourmaline": 0.12,
        "fluorite": 0.11
    }

    # Quality multipliers
    quality_multipliers = {
        "A": 1.5,
        "B": 1.2,
        "C": 1.0
    }

    # Cut/shape multipliers
    cut_multipliers = {
        "raw": 1.0,
        "tumbled": 1.2,
        "polished": 1.4,
        "tower": 1.6,
        "sphere": 1.8
    }

    # Get base price
    base_price = base_prices.get(stone.lower(), 0.10)

    # Get multipliers
    quality_multiplier = quality_multipliers.get(quality.upper(), 1.0)
    cut_multiplier = cut_multipliers.get(cut.lower(), 1.0)

    # Calculate wholesale value
    wholesale = weight_grams * base_price * quality_multiplier * cut_multiplier

    # Retail range (2x–3x markup)
    retail_low = wholesale * 2
    retail_high = wholesale * 3

    return {
        "stone": stone,
        "weight": weight_grams,
        "wholesale_estimate": round(wholesale, 2),
        "retail_range": (round(retail_low, 2), round(retail_high, 2))
    }


# Example usage
if __name__ == "__main__":
    result = calculate_price(
        stone="labradorite",
        weight_grams=120,
        quality="A",
        cut="polished"
    )
    print(result)
