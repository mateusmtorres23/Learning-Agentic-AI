CREATE TYPE transaction_type_enum AS ENUM ('DEPOSIT', 'WITHDRAWAL', 'TRANSFER', 'PAYMENT', 'REFUND');

CREATE TYPE entry_mode_enum AS ENUM ('CHIP', 'NFC', 'MAGNETIC_STRIPE', 'MANUAL_ENTRY', 'ONLINE_FORM');

CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_number VARCHAR(20) NOT NULL,
    card_number VARCHAR(20) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_type transaction_type_enum NOT NULL,
    transaction_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    country CHAR(2) NOT NULL,
    entry_mode entry_mode_enum NOT NULL
);

INSERT INTO transactions (account_number, card_number, amount, transaction_type, country, entry_mode)
SELECT
    LPAD(FLOOR(random() * 9999999999)::BIGINT::TEXT, 10, '0'),
    LPAD(FLOOR(random() * 9999999999999999)::BIGINT::TEXT, 16, '0'),
    (random() * 9999.99 + 0.01)::DECIMAL(10, 2),
    (ARRAY['DEPOSIT', 'WITHDRAWAL', 'TRANSFER', 'PAYMENT', 'REFUND'])[FLOOR(random() * 5 + 1)]::transaction_type_enum,
    (ARRAY['BR', 'US', 'UK', 'JP', 'CA'])[FLOOR(random() * 5 + 1)],
    (ARRAY['CHIP', 'NFC', 'MAGNETIC_STRIPE', 'MANUAL_ENTRY', 'ONLINE_FORM'])[FLOOR(random() * 5 + 1)]::entry_mode_enum
FROM generate_series(1, 1000);

SELECT * FROM transactions