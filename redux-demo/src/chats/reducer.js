import { REPLY_MESSAGE, SEND_MESSAGE, START_CHAT } from "./types"

const initialState = {
	chats: 0,
	messages: 0,
}

const reducer = (state = initialState, action) => {
	switch(action.type) {
		case START_CHAT:
			return {
				...state,
				chats: state.chats + 1, // todo: increment operator
				messages: state.messages + 1, // todo: increment operator
			}
		case SEND_MESSAGE:
			return {
				...state,
				chats: state.chats + 1, // todo: increment operator
				messages: state.messages + 1, // todo: increment operator
			}
		case REPLY_MESSAGE:
			return {
				...state,
				messages: state.messages + 1, // todo: increment operator
			}
		default:
			return state
	}
}