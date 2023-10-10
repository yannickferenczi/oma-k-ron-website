const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
const clientSecret = $("#id_client_secret").text().slice(1, -1);

const stripe = Stripe(stripePublicKey);

const appearance = {
    theme: 'stripe',
    variables: {
        fontWeightNormal: '500',
        borderRadius: '2px',
        colorPrimary: '#f360a6',
        colorIconTabSelected: '#fff',
        spacingGridRow: '16px'
    },
    rules: {
        '.Tab, .Input, .Block, .CheckboxInput, .CodeInput': {
            boxShadow: '0px 3px 10px rgba(18, 42, 66, 0.08)'
        },
        '.Block': {
            borderColor: 'transparent'
        },
        '.BlockDivider': {
            backgroundColor: '#fff'
        },
        '.Tab, .Tab:hover, .Tab:focus': {
            border: '0'
        },
        '.Tab--selected, .Tab--selected:hover': {
            backgroundColor: '#f360a6',
            color: '#fff'
        }
    }
};

const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'usd',
    appearance: appearance,
};

const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');

let card = elements.create("card");
card.mount("#card-element");
