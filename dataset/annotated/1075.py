def get_fighter_statement(fighter: str) -> str:
    statements = {
        'george saint pierre': "I am not impressed by your performance.",
        'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    }
    return statements[fighter.lower()]

