const initialState = {
    questions: [],
    fetching: false,
    fetched: false,
    error: null
}

export default function reducer(state=initialState, action) {
    switch (action.type) {
        case "FETCH_QUESTIONS_PENDING":
            return {...state, fetching: true};
        case "FETCH_QUESTIONS_FULFILLED":
            return {...state, fetching: false, fetched: true, questions: action.payload.data};
        case "FETCH_QUESTIONS_REJECTED":
            return {...state, fetching: false, error: action.payload};
    }
    return state;
}