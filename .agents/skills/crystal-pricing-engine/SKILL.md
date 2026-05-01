---
name: crystal-pricing-engine
description: Calculates estimated wholesale and retail pricing ranges for crystals based on weight, quality, and cut. Use when the user wants structured, repeatable pricing for crystal products.
---

## When to use this skill
Use this skill when:
- The user provides details about a crystal (type, weight, quality, cut)
- The user wants a consistent pricing estimate rather than a general guess
- Pricing needs to be calculated using repeatable rules

## When NOT to use this skill
Do NOT use this skill when:
- The user asks for general crystal knowledge or metaphysical properties
- The user wants market trends or external pricing data
- The user expects a certified appraisal or exact resale value

## Expected inputs
The skill expects structured inputs:
- stone (string): type of crystal (e.g., labradorite, amethyst)
- weight_grams (number): weight of the item in grams
- quality (string): A, B, or C
- cut (string): raw, tumbled, polished, tower, or sphere

## Instructions
1. Extract structured input values from the user’s request.
2. Call the Python script in `scripts/price_calculator.py`.
3. Pass the extracted values into the `calculate_price` function.
4. Receive the calculated pricing output.
5. Present the results clearly to the user.

## Output format
Return a structured summary including:
- Stone type
- Weight
- Estimated wholesale value
- Suggested retail price range

Example:

Stone: Labradorite  
Weight: 120g  
Estimated Wholesale: $18.00  
Suggested Retail Range: $36.00 – $54.00  

## Limitations and notes
- Pricing is based on simplified internal rules, not live market data
- Results are estimates and should not be used as formal appraisals
- Base price tables and multipliers can be extended or adjusted
