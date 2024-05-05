import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, TouchableOpacity, ScrollView, Image } from 'react-native';
import { FontAwesome } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';

const CHAT_BOT_FACE = 'https://res.cloudinary.com/dknvsbuyy/image/upload/v1685678135/chat_1_c7eda483e3.png';

export default function ChatScreen() {
    const [messages, setMessages] = useState([]);
    const [inputText, setInputText] = useState('');

    const onSend = async () => {
        if (!inputText.trim()) return;

        // Construct user message
        const userMessage = {
            _id: messages.length + 1,
            text: inputText,
            createdAt: new Date(),
            user: {
                _id: 1,
                name: 'User',
                avatar: null,
            },
        };

        setMessages([...messages, userMessage]);
        setInputText('');

        try {
            
            const resp = await fetch('http://127.0.0.1:8000/api/legal_query/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: inputText }),
            });
            const responseData = await resp.json();

            
            const chatBotResponse = {
                _id: messages.length + 2,
                text: responseData.result,
                createdAt: new Date(),
                user: {
                    _id: 2,
                    name: 'Chat Bot',
                    avatar: CHAT_BOT_FACE,
                },
            };

            setMessages([...messages, chatBotResponse]);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <View style={{ flex: 1, backgroundColor: '#fff', padding: 10 }}>
            <ScrollView
                ref={(ref) => (this.scrollView = ref)}
                onContentSizeChange={() => {
                    this.scrollView.scrollToEnd({ animated: true });
                }}
            >
                {messages.map((message) => (
                    <View key={message._id} style={{ flexDirection: 'row', alignItems: 'flex-end' }}>
                        {message.user._id === 1 ? null : (
                            <Image
                                source={{ uri: message.user.avatar }}
                                style={{ width: 40, height: 40, borderRadius: 20, marginRight: 8 }}
                            />
                        )}
                        <View
                            style={{
                                backgroundColor: message.user._id === 1 ? '#671ddf' : '#fff',
                                borderRadius: 8,
                                paddingHorizontal: 12,
                                paddingVertical: 8,
                                margin: 4,
                            }}
                        >
                            <Text style={{ color: message.user._id === 1 ? '#fff' : '#000' }}>{message.text}</Text>
                        </View>
                    </View>
                ))}
            </ScrollView>
            <View style={{ flexDirection: 'row', alignItems: 'center', paddingHorizontal: 8 }}>
                <TextInput
                    style={{ flex: 1, borderWidth: 1, borderRadius: 20, paddingVertical: 8, paddingHorizontal: 16, borderColor: '#671ddf', marginRight: 8 }}
                    placeholder="Type your message here"
                    value={inputText}
                    onChangeText={(text) => setInputText(text)}
                />
                <TouchableOpacity onPress={onSend}>
                    <FontAwesome name="send" size={24} color="#671ddf" />
                </TouchableOpacity>
            </View>
        </View>
    );
}
