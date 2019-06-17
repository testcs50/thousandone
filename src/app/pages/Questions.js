import React from 'react';
import {connect} from 'react-redux';

import fetchQuestions from '../actions/questionsAction';

import Question from '../components/Question';

class Questions extends React.Component {
    render() {
        let questions = this.props.questions.map((item, index) => {
            return <Question key={index}>{item}</Question>
        })
        return (
            <div>
                <h1>Questions</h1>
                <ol>
                    {questions}
                </ol>
            </div>
        )
    }
    componentDidMount() {
        this.props.dispatch(fetchQuestions())
    }
}

function mapStateToProps(state) {
    return {
        questions: state.questions
    }
}

export default connect(mapStateToProps)(Questions)