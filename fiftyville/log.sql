-- Keep a log of any SQL queries you execute as you solve the mystery.

--TO CHECK WHAT HAPPENED ON HUMPHREY STREET AT THE DAY OF THE CRIME
SELECT description FROM crime_scene_reports
WHERE month = 7 and day = 28 AND street = "Humphrey Street";

--TO CHECK WHAT HAPPENED AT THE BAKERY AT 10:15
SELECT * FROM bakery_security_logs
WHERE day = 28 AND month = 7 AND hour = 10;
--TO CHECK THE DETAILS OF THE INTERVIEWS AND GATHER CLUES
SELECT * FROM interviews WHERE transcript LIKE "%bakery%";

--TO CHECK THE ACCOUNT_NUMBER BY LOOKING AT THE ATM LOGS
SELECT * FROM atm_transactions
WHERE day = 28 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";

--TO CHECK ALL THE FLIGHTS HAPPENED THAT DAY SO WE KNOW ITS THE EARLIEST ONE
SELECT * FROM flights WHERE day = 29 AND month = 7;
--TO FIND THE ID FROM THE FLIGHT WHICH WE KNOW BECAUSE IT WAS THE EARLIEST ONE
SELECT * FROM airports
JOIN flights ON airports.id = flights.origin_airport_id
WHERE day = 29 AND month = 7 AND city = "Fiftyville";
--TO FIND THE DESTINATION OF THE FLIGHT ID WE KNOW THE FLEW
SELECT * FROM airports
JOIN flights ON airports.id = flights.destination_airport_id
WHERE day = 29 AND month = 7;


--
SELECT * FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id;
--
SELECT * FROM phone_calls
WHERE day = 28 AND month = 7 AND duration < 60;
--
SELECT * FROM passengers
JOIN flights ON flights.id = passengers.flight_id
JOIN airports ON airports.id = flights.destination_airport_id
WHERE destination_airport_id = 4 AND origin_airport_id = 8 AND month = 7 AND day = 29;
-- TO FIND THE PERSON THAT THIS PASSPORT_NUMBER BELONGS TO
SELECT * FROM people WHERE passport_number = 5772159633;