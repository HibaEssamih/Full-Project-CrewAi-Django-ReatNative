import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, ScrollView, ActivityIndicator, StyleSheet } from 'react-native';
import { FontAwesome } from '@expo/vector-icons';

export default function ChatScreen() {
    const [chatHistory, setChatHistory] = useState([]);
    const [inputText, setInputText] = useState('');
    const [loading, setLoading] = useState(false);

    const onSend = async () => {
        if (!inputText.trim() || loading) return;

        setLoading(true);

        try {
            const formData = new FormData();
            formData.append('query', inputText);

            chatHistory.forEach((message, index) => {
                formData.append(`history[${index}][type]`, message.type);
                formData.append(`history[${index}][text]`, message.text);
                formData.append(`history[${index}][createdAt]`, message.createdAt.toISOString());
            });

            const resp = await fetch(`http://192.168.1.3:8000/api/document_generation_check/`, {
                method: 'POST',
                body: formData,
            });

            const responseData = await resp.json();

            const userMessage = {
                type: 'user',
                text: inputText,
                createdAt: new Date(),
            };

            const chatBotResponse = {
                type: 'bot',
                text: responseData.result,
                createdAt: new Date(),
            };

            const newChatHistory = [...chatHistory, userMessage, chatBotResponse];

            if (responseData.information) {
                const infoMessage = {
                    type: 'bot',
                    text: responseData.information,
                    createdAt: new Date(),
                };
                newChatHistory.push(infoMessage);
            }

            setChatHistory(newChatHistory);
            setInputText('');
        } catch (error) {
            console.error('Error:', error);
        } finally {
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
                {chatHistory.map((message, index) => (
                    <View key={index} style={{ flexDirection: message.type === 'user' ? 'row-reverse' : 'row', paddingHorizontal: 8 }}>
                        <View
                            style={{
                                backgroundColor: message.type === 'user' ? '#eeeeee' : '#671ddf',
                                borderRadius: 8,
                                paddingHorizontal: 12,
                                paddingVertical: 8,
                                maxWidth: '70%',
                                marginVertical: 4,
                                alignSelf: 'flex-start',
                            }}
                        >
                            <Text style={{ color: message.type === 'user' ? '#000' : '#fff' }}>{message.text}</Text>
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
