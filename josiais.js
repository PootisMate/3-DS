import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, 
Alert, StyleSheet} from 'react-native';

export default function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const handleLogin = () => {
    if (!email || !password)  {
      Alert.alert('Erro', 'Por favor, preencha todos os campos.');
      return;   
    }
    Alert.alert('Sucesso', `Bem-vindo, ${email}!`);
  };
  return (
    <View style={styles.container}>
     <Text style={styles.titles}>Login</Text>

     <TextInput 
      style={styles.input}
      placeholder="E-mail"
      keyboardType="email-address"
      autoCapitalize="none"
      value={email}
      onChangeText={setEmail}
      />
      <TextInput
      style={styles.input}
      placeholder="Numero do cartão de crébito"
      secureTextEntry
      value={password}
      onChangeText={setPassword}
      />

      <TouchableOpacity style={styles.button} onPress={handleLogin}>
       <Text style={styles.buttonText}>Entrar</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f4f4f4',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    width: '80%',
    height: 50, 
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 8,
    paddingHorizontal: 10,
    backgroundColor: '#fff',
    marginBottom: 15,
  },
  button: {
    backgroundColor: '#007bff',
    paddingVertical: 12,
    paddingHorizontal: 40,
    borderRadius: 8,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold' 
  },
 });
