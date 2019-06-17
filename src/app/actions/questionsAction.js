import axios from 'axios';

export default function () {
    return {
        type: 'FETCH_QUESTIONS',
        payload: axios.get('/get-questions')
    }
}

// export default {
//     type: 'FETCH_QUESTIONS',
//     payload: axios.get('/get-questions')
// }