import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, ScrollView, ActivityIndicator, Image, StyleSheet } from 'react-native';
import { FontAwesome } from '@expo/vector-icons';

const CHAT_BOT_FACE = 'https://res.cloudinary.com/dknvsbuyy/image/upload/v1685678135/chat_1_c7eda483e3.png';

export default function ChatScreen() {
    const [messages, setMessages] = useState([]);
    const [inputText, setInputText] = useState('');
    const [loading, setLoading] = useState(false);

    const onSend = async () => {
        if (!inputText.trim() || loading) return;

        // Disable send button and show loading indicator
        setLoading(true);

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
            const formData = new FormData();
            formData.append('query', inputText);
            const resp = await fetch(`http://192.168.1.14:8000/api/legal_assistance_check/`, {
                method: 'POST',
                body: formData,
            });

            const responseData = await resp.json();

            // Check if responseData.result is defined
            if (responseData.result) {
                // Extract and format the result from the response
                const formattedResult = responseData.result.replace(/\n\n/g, '\n').replace(/\n\n\*/g, '\n\n•').replace(/\*+/g, '');

                // Construct chat bot response
                const chatBotResponse = {
                    _id: messages.length + 2,
                    text: formattedResult,
                    createdAt: new Date(),
                    user: {
                        _id: 2,
                        name: 'Chat Bot',
                        avatar: CHAT_BOT_FACE,
                    },
                };

                // Add chat bot response after user message
                setMessages([...messages, userMessage, chatBotResponse]);
            } else {
                console.error('Error: Response data does not contain result:', responseData);
            }
        } catch (error) {
            console.error('Error:', error);
        } finally {
            // Re-enable send button and hide loading indicator
            setLoading(false);
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
                {messages.map((message, index) => (
                    <View key={message._id} style={{ flexDirection: 'row', paddingHorizontal: 8 }}>
                        {message.user._id === 1 ? ( // User's message
                            <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end', marginVertical: 4 }}>
                                <View
                                    style={{
                                        backgroundColor: '#eeeeee',
                                        borderRadius: 8,
                                        paddingHorizontal: 12,
                                        paddingVertical: 8,
                                        maxWidth: '70%',
                                    }}
                                >
                                    <Text style={{ color: '#000' }}>{message.text}</Text>
                                </View>
                            </View>
                        ) : ( // Chat Bot's response
                            <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-start', marginVertical: 4 }}>
                                <View
                                    style={{
                                        backgroundColor: '#671ddf',
                                        borderRadius: 8,
                                        paddingHorizontal: 12,
                                        paddingVertical: 8,
                                        maxWidth: '70%',
                                    }}
                                >
                                    <Text style={{ color: '#fff' }}>{message.text}</Text>
                                </View>
                            </View>
                        )}
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
                <TouchableOpacity onPress={onSend} disabled={loading} style={[styles.sendButton, loading && styles.sendButtonDisabled]}>
                    <FontAwesome name="send" size={24} color="#fff" />
                </TouchableOpacity>
            </View>
            {loading && (
                <View style={styles.loadingContainer}>
                    <ActivityIndicator color="#671ddf" size="large" />
                </View>
            )}
        </View>
    );
}

const styles = StyleSheet.create({
    sendButton: {
        backgroundColor: '#671ddf',
        borderRadius: 20,
        padding: 10,
    },
    sendButtonDisabled: {
        opacity: 0.5,
    },
    loadingContainer: {
        ...StyleSheet.absoluteFillObject,
        backgroundColor: 'rgba(255, 255, 255, 0.5)',
        justifyContent: 'center',
        alignItems: 'center',
    },
});
